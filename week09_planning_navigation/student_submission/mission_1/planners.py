"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    start = ctx.start
    goal = ctx.goal

    #Check if the start or goal is an obstacle or if they are the same
    if ctx.grid[start[0]][start[1]] == 1 or ctx.grid[goal[0]][goal[1]] == 1:
        return []
    if start == goal:
        return [start]

    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            return reconstruct(parent, goal)
        #Look at all available neighbors of the current cell
        for neighbor in ctx.expand(current, len(queue) + 1):
            #Did we discover this cell before?
            if neighbor not in parent:
                #Remember which cell we came from to reach this neighbor
                parent[neighbor] = current
                #Add the new cell to the queue so we can explore it later
                queue.append(neighbor) 
    #If the queue is empty and we haven't found the goal, return an empty list (aka no route found)                 
    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    start = ctx.start
    goal = ctx.goal

    #Check if the start or goal is an obstacle or if they are the same
    if ctx.grid[start[0]][start[1]] == 1 or ctx.grid[goal[0]][goal[1]] == 1:
        return []
    if start == goal:
        return [start]

    stack = [start]
    parent = {start: None}

    while stack:
        current = stack.pop()
        if current == goal:
            return reconstruct(parent, goal)
        neighbors = ctx.expand(current, len(stack) + 1) 
        #Using reversed() to preserve the original neighbour order for DFS because of the LIFO stack nature
        for neighbor in reversed(neighbors):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)
    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    start = ctx.start
    goal = ctx.goal

    #Check if the start or goal is an obstacle or if they are the same
    if ctx.grid[start[0]][start[1]] == 1 or ctx.grid[goal[0]][goal[1]] == 1:
        return []
    if start == goal:
        return [start]

    depth_limit = 0
    while True:
        cutoff = False
        stack = [(start, 0, [start])]  #(cell, depth, path)
        while stack:
            current, depth, path = stack.pop()
            if current == goal:
                return path
            #Get neighbors of the current cell
            neighbors = ctx.expand(current, len(stack) + 1)
            #Check if we have reached the depth limit
            if depth >= depth_limit:
                if any(neighbor not in path for neighbor in neighbors):
                    cutoff = True
                continue
            #Add neighbors to the stack if they are not already in the current path
            for neighbor in reversed(neighbors):
                if neighbor not in path:
                    stack.append((neighbor, depth + 1, path + [neighbor]))

        #Stop if there are no more paths to explore within the current depth limit
        if not cutoff:
            return []
        #Increase the depth limit for the next iteration
        depth_limit += 1


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    start = ctx.start
    goal = ctx.goal

    #Check if the start or goal is an obstacle or if they are the same
    if ctx.grid[start[0]][start[1]] == 1 or ctx.grid[goal[0]][goal[1]] == 1:
        return []
    if start == goal:
        return [start]
    
    queue = []
    parent = {start: None}
    g_score = {start: 0}
    #Add the starting cell to the priority queue
    heappush(queue, (ctx.heuristic(start), 0, start))  #(f, g, cell)

    while queue:
        #Get the cell with the lowest f value (aka cost) from the priority queue
        f, g, current = heappop(queue)
        #Skip this cell if we have already found a better path to it
        if g > g_score[current]:
            continue
        if current == goal:
            return reconstruct(parent, goal)
        #Explore neighbors of the current cell
        for neighbor in ctx.expand(current, len(queue) + 1):
            new_g = g + 1
            #Update the g score and parent if we found a better path to the neighbor
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                parent[neighbor] = current
                #Calculate the estimated total cost f = g + h for the neighbor
                new_f = new_g + ctx.heuristic(neighbor)
                heappush(queue, (new_f, new_g, neighbor))

    return []



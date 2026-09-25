# Mission 3

## Specification

The robot should move in a rounded rectangle. It should move straight for 0.40 m, make a 90 degree left arc,  move straight for 0.25 m, and make another 90 degree left arc. The robot needs to repeat this pattern twice in order to complete the rounded rectangle. I would use a linear speed of 0.15 m/s  for the straight parts and 0.12 m/s with an angular speed of 0.80 rad/s for the arcs. After finishing all eight parts, the robot should stop near where it started. Each straight distance should be within 0.02 m, each turn is within 0.04 rad of 90 degrees, and the arc radius is within 0.02 m of 0.15 m.

## Saved Specification

The robot should move in a rounded rectangle. It should move straight for 0.40 m, make a 90 degree left arc,  move straight for 0.25 m, and make another 90 degree left arc. The robot needs to repeat this pattern twice in order to complete the rounded rectangle. I would use a linear speed of 0.15 m/s  for the straight parts and 0.12 m/s with an angular speed of 0.80 rad/s for the arcs. After finishing all eight parts, the robot should stop near where it started. Each straight distance should be within 0.02 m, each turn is within 0.04 rad of 90 degrees, and the arc radius is within 0.02 m of 0.15 m.

## Assigned Pattern

rounded_rectangle

## Original Prompt

The robot should move in a rounded rectangle. It should move straight for 0.40 m, make a 90 degree left arc, move straight for 0.25 m, and make another 90 degree left arc. The robot needs to repeat this pattern twice in order to complete the rounded rectangle. I would use a linear speed of 0.15 m/s  and no angular velocity for the straight parts, and a linear speed of 0.12 m/s with an angular speed of 0.80 rad/s for the arcs. After finishing all eight parts, the robot should stop near where it started. Each straight distance should be within 0.02 m, each turn should be within 0.04 rad of 90 degrees, and the arc radius should be within 0.02 m of 0.15 m.

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'rounded_rectangle' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.


## Original Output

### Assumptions

I assume the rounded rectangle has **8 segments total**: four straight segments and four 90-degree left arcs.

For the straight sections, the robot moves at `0.15 m/s`. The duration of each straight section can be calculated using distance divided by speed:

* 0.40 m straight: `0.40 / 0.15 ≈ 2.67 seconds`
* 0.25 m straight: `0.25 / 0.15 ≈ 1.67 seconds`

For the arcs, the robot moves at `0.12 m/s` while turning left at `0.80 rad/s`. This produces a radius of `0.12 / 0.80 = 0.15 m`. A 90-degree turn is π/2 radians, so each arc should last:

`(π / 2) / 0.80 ≈ 1.96 seconds`

All speeds and durations are within the required limits.

### Implementation

Assuming `Segment` is already defined in `pattern.py`, `build_pattern` can be implemented as:

```python
import math


def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    straight_speed = 0.15
    arc_linear_speed = 0.12
    arc_angular_speed = 0.80

    long_duration = 0.40 / straight_speed
    short_duration = 0.25 / straight_speed
    arc_duration = (math.pi / 2) / arc_angular_speed

    return [
        Segment(straight_speed, 0.0, long_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, short_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, long_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, short_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
    ]
```

The course wrapper should handle repeatedly publishing these segments and sending the final zero command, so `build_pattern` does not need to publish anything itself.

### Proposed tests

I would test that:

* `build_pattern("rounded_rectangle")` returns exactly **8 segments** in the correct order.
* The straight segments represent distances of **0.40 m, 0.25 m, 0.40 m, and 0.25 m**.
* Each arc produces a **90-degree left turn** with a radius of **0.15 m**.
* Linear and angular speeds stay within the required limits.
* Each segment is under 30 seconds and the entire pattern is under 60 seconds.
* An unknown pattern name raises `ValueError`.


## Original Source

import math


def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    straight_speed = 0.15
    arc_linear_speed = 0.12
    arc_angular_speed = 0.80

    long_duration = 0.40 / straight_speed
    short_duration = 0.25 / straight_speed
    arc_duration = (math.pi / 2) / arc_angular_speed

    return [
        Segment(straight_speed, 0.0, long_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, short_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, long_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, short_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
    ]

## Assumptions

The AI assumed that the robot moves at the constant speed during each part so that it could calculate each duration from the distance and speed. It also assume that the robot starts each segment immediately after the previous one and that the course wrapper takes care of publishing the commands and making the robot come to a stop at the end.

## Problems

I didn't find any obvious errors, but I double checked the calculations to make sure they were correct. I also checked the duration for the straight parts, the radius and duration of the arcs, and that all eight parts were in the right order. I made sure that the speeds and durations were within the given limits. 

## Test Plan

For the patter behavior test, I would check that the robot completes all eight segments in the correct order and that it finished near where it started. I am expecting to see a rounded rectangle with four straight parts and four 90 degree left arcs. For the velocity-limit test, I would make sure that the linear speed never exceeds 0.22 m/s and that the angular speed never exceeds 0.80 rad/s. I am expecting that all segments stay within these limits. For the stop test, I would make sure that both linear and angular velocity are set to 0. I am expecting that the robot comes to a complete stop after completing the rectangle.

## Modifications

I made two changes to the original code. I added separate variables for the long distance, short distance, and turn angle instead of putting the values directly into the duration calculations because I think it makes the calculations easier to understand. I also replace the repeated list of eight segments with a for loop because the same four segments are repeated twice. So it made more sense to me to have a for loop which reduces repetition and makes the code shorter.

## Live Pending

True

## Evidence Analysis

The tests establish that my code follows the rounded rectangle pattern and stays within the required limits. All 9 tests passed, including the two I wrote to check the number and order of the segments as well as the distances of the straight parts. The tests also proved that the command limits and stop decision behave as expected. With that being said, the tests can't guarantee that the robot will behave identically on every run. One additional test I would need is to run the robot from different starting points to make sure that it still completes the pattern as expected and stops correctly.

## Ai Disclosure

I used ChatGPT to help me generate the initial code based on my prompt and understand what the generated code was doing. I also used it to help me troubleshoot my issue with live verification not working. I personally checked the speeds, durations, segment order, and calculations. I also changed the code to reduce repetition and make it easier to understand. Lastly, I wrote two tests to check the geometry and order of the segments. 

## Live Issue

I am not sure if I am running it incorrectly but it worked on my screen. I ran python3 scripts/run_assigned_pattern.py --live and saw the robot move and the terminal looks just fine. I am not sure why the lab is not reflecting it. 

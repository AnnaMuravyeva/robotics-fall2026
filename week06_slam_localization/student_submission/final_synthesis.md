# Final synthesis

From the two attempts at mapping, I learned that the robot can use its motion estimates and LiDAR scans to build a map of its surroundings, but it is challenging to do so well. It is hard for a robot to determine the exact positions of walls and obstacles . LiDAR can identify walls and open spaces, but its view can be blocked by things like obstacles, which is why some of the areas remained unknown or were poorly outlined.

My first route took 20 minutes to complete, while my second route took 94 minutes. For the second route, I changed my approach from simply visiting each room once to exploring the perimeter of each room and revisiting each area at least once. This improved the known area from 115.9 m^2 to 147.38 m^2 and the quality score went up from 47.1 to 73.9.

With that being said, the second map was far from perfect. It still had problems with overlapping and duplicated walls, especially on the right side of the house. I kept revisiting that area, hoping to fix the issues, but it just kept getting worse. This could possibly be the result of errors in the robot's motion estimates building up over time. This shows that even though SLAM can correct these errors when revisiting an area, it doesn't always work.

Overall, I think the second map is more trustworthy, as it shows more of the house and has clearer room outlines. But, neither map is guaranteed to be fully accurate. Both would need to be compared with the actual layout of the house to determine how truly accurate they are.

# Mission 3

## Data To Command

The front_distance() function takes the list of LiDAR distances and finds the nearest valid distance in front of the robot. The decide_velocity() function then uses that distance to determine whether the robot should move forward or come to a stop depending on whether the obstacle is within the stop distance 

## Missing Data Safety

The robot stop when there is no valid front measurement instead of treating the path as clear because without a valid measurement, there is no way for it to know whether the path ahead is actually clear. Stopping is safer than assuming there is no obstacle and possibly causing the robot to crash 

## System Layers

My decision functions use the LiDAR readings to determine whether the robot should move or stop. The supplied ROS node receives the /scan data, calls my functions, and publishes the resulting command to /student_cmd_vel. The command guard checks that command to make sure it is valid and safe before publishing it to /cmd_vel, which controls the robot

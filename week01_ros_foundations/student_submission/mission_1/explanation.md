# Mission 1

## Architecture Observation

I would say the observed system is mostly reactive. Commands are received and passed through the command guard to control the robot as sensor data such as /scan and /odom is continuously published. 

## Connections

{'guard_input': '/student_cmd_vel', 'guard_output': '/cmd_vel', 'lidar_output': '/scan', 'odometry_output': '/odom', 'teleop_output': '/student_cmd_vel'}

## Failure Diagnosis

If the /student_cmd_vel connection were missing, the command guard wouldn't receive the teleoperation velocity commands. This would cause the robot to not move when the user tries to control it

## Middleware Evidence

ROS 2 provides communication between programs. The live ROS graph shows separate nodes communicating through ROS 2 topics and services. One example would be /course_cmd_vel_guard which receives commands through /student_cmd_vela nd send them through /cmd_vel. 

## Multiple Subscribers

Because of the publish/subscribe system. A publisher sends data to a topic and multiple nodes can subscribe to the same topic and receive the data independently 

## Node Roles

{'/course_cmd_vel_guard': 'Decision/control', '/course_evidence_collector': 'Infrastructure', '/robot_state_publisher': 'Infrastructure', '/ros_gz_bridge': 'Simulation', '/rviz2': 'Visualization'}

## Node Vs Topic

A node is a program that performs a specific task, while a topic is a communication channel used by nodes to send and receive data

## Pipeline Roles

{'/course_cmd_vel_guard': 'Decide', '/course_evidence_collector': 'Support', '/robot_state_publisher': 'Support', '/ros_gz_bridge': 'Support', '/rviz2': 'Support'}

## Rviz Role

RViz is an observer because it visualizes information from the ROS system. Even though it publishes topics such as /clicked_point, /goal_pose, and /initialpose, it doesn't publish movement commands on /cmd_vel, so it is not directly controlling the robot. 

## Sense Decide Act

The LiDAR/simulator sense the environment and publishes gathered information on /scan. The command guard is part of decision because it processes movement commands and lastly the robot controller acts on the commands coming from /cmd_vel to move the robot

## Service Example

{'name': '/course_cmd_vel_guard/describe_parameters ', 'purpose': "It likely receives a request asking for information about the command guard's parameters and it responds with the descriptions of those parameters", 'type': 'rcl_interfaces/srv/DescribeParameters'}

## Service Vs Topic

A topic carries a stream of messages between publishers and subscribers, while a service uses a request and response system. A specific example from the lab would be /student_cmd_vel that carries velocity commands as a topic. On the other hand /course_cmd_vel_guard/get_parameters is a service that receives a request and returns a response 

## Teleop Change

When teleoperation starts 

## Topic Types

{'/odom': 'nav_msgs/msg/Odometry', '/scan': 'sensor_msgs/msg/LaserScan', '/student_cmd_vel': 'geometry_msgs/msg/Twist'}

## Scan Observation

I found several +inf values in the range field, which represent directions where the LiDAR didn't detect an object within its min/max range. 

## Guided Checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## Graph Explanation

A ROS 2 graph shows software components that are currently running and how they are connected with one another. For example, it would show that the /ros_gz_bridge node publishes messages to the /scan topic, and the /course_evidence_collector node subscribes to /scan and receives the messages

## Command Path Explanation

A proposed command travels on  the /student_cmd_vel topic. The guard performs a safety check to make sure that the proposed command is safe and valid. Then it publishes the given command on /cmd_vel so that it reaches the robot

## Tools Explanation

Gazebo is responsible for simulating the robot and its physical environment. It simulates things that would happen physically, like robot's location, how its wheels move, where the walls are, and more. While RViz is responsible for displaying ROS 2 data such as the robot's position and sensor readings. In other words, Gazebo simulates what is actually happening to the robot, while RViz shows us the information that ROS 2 has about the robot and world around it

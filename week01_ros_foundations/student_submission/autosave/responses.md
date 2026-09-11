# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Anna Muravyeva
- Email: 24462672

## final.architecture_evidence

My node is reactive because it uses the current LiDAR readings to immediately decided whether the robot should move or stop. It doesn't have a plan for what comes next. For it to be a genuinely hybrid system we would need to add a planning component that makes longer term decision and keep the reactive layer for immediate responses to obstacles

## final.course_reflection

This activity definitely made me more interested in learning about robotics . Before this lab, ROS 2 felt somewhat overwhelming, but working through the system piece by piece made it a lot easier to understand. What stood out to me the most was seeing the robot move in the simulation. Even though we only had to implement small parts of an already provided system, it was still super exciting to see everything come together. I am definitely looking forward to working on more complex problems in the future. 

## final.hardware_next

Before using the behavior on hardware, I would test more edge cases and sensor failures such as invalid LiDAR readings, obstacles placed exactly at the stop distance, unexpected obstacles, and loss of communication. Overall, I would make sure that the robot consistently stops at a safe distance before allowing it to operate on real hardware

## final.middleware_debugging

The ROS graph would help me diagnose a command that never reaches the robot by letting me trace the command through its publishers, topics, and subscribers to determine where the communication fails. For example, I could check whether /obstacle_guard is publishing to /student_cmd_vel, and whether the command guard is receiving it, and whether a command is then being published to /cmd_vel. This would help me identify exactly where the command stops and what is preventing it from reaching the robot

## final.system_synthesis

Robotics software is difficult because a robot has to receive information from sensors, make decisions based on that information, and control its physical movement. At the same time, it has to also deal with things like missing or invalid data and timing issues. A mistake in robotics software could cause the robot to move in an unsafe way leading to potentially severe consequences. 

In this lab, I implemented a reactive architecture. The robot uses its current LiDAR readings to immediately decide whether to move or stop with no plan for what comes next. The front_distance() function goes through the LiDAR readings, searching for the closest valid distance in front of the robot. Then decide_velocity() uses that distance to decide whether the robot should move forward or come to a stop. This architecture is simple and allows the robot to quickly respond to obstacles, but it only reacts to the information it currently has with no plan on how to get to a certain destination.

ROS 2 middleware allows the different components of the system to communicate using topics. The /ros_gz_bridge publishes LiDAR readings to /scan. The /obstacle_guard node subscribes to /scan, uses front_distance() and decide_velocity() functions to decide whether the robot should move, and publishes the potential command to /student_cmd_vel. Then the command guard reviews it to make sure that the proposed command is safe and valid before publishing it to /cmd_vel which will move the robot. This shows how multiple parts of the system can work together without needing to communicate directly with one another.

Timing and invalid sensor data are important for safety. For example, if front_distance() can't find a valid LiDAR reading, then decide_velocity() returns 0 because without a valid reading we can't simply assume that the path is clear. The timeout also stops the robot if it doesn't receive a new command within 0.5 seconds to protect it in case the communication is lost or the program crashes.  The command guard provides another layer of safety by checking proposed commands to make sure that they are valid and safe before they reach the robot. So even if unsafe movement is proposed, the command guard will stop it from being executed.

## final.timing_evidence

The sensor-failure result that affected my understanding the most was seeing the robot stop when there was no valid LiDAR measurement instead of assuming that the path is clear. It  made me realize that missing or invalid sensor data can be a safety issue since that's the only way for the robot to know what is happening around it and wether there is an obstacle in front of it or not

## mission_1.architecture_observation

I would say the observed system is mostly reactive. Commands are received and passed through the command guard to control the robot as sensor data such as /scan and /odom is continuously published. 

## mission_1.command_path_explanation

A proposed command travels on  the /student_cmd_vel topic. The guard performs a safety check to make sure that the proposed command is safe and valid. Then it publishes the given command on /cmd_vel so that it reaches the robot

## mission_1.connections

{'guard_input': '/student_cmd_vel', 'guard_output': '/cmd_vel', 'lidar_output': '/scan', 'odometry_output': '/odom', 'teleop_output': '/student_cmd_vel'}

## mission_1.failure_diagnosis

If the /student_cmd_vel connection were missing, the command guard wouldn't receive the teleoperation velocity commands. This would cause the robot to not move when the user tries to control it

## mission_1.graph_explanation

A ROS 2 graph shows software components that are currently running and how they are connected with one another. For example, it would show that the /ros_gz_bridge node publishes messages to the /scan topic, and the /course_evidence_collector node subscribes to /scan and receives the messages

## mission_1.guided_checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## mission_1.middleware_evidence

ROS 2 provides communication between programs. The live ROS graph shows separate nodes communicating through ROS 2 topics and services. One example would be /course_cmd_vel_guard which receives commands through /student_cmd_vela nd send them through /cmd_vel. 

## mission_1.multiple_subscribers

Because of the publish/subscribe system. A publisher sends data to a topic and multiple nodes can subscribe to the same topic and receive the data independently 

## mission_1.node_roles

{'/course_cmd_vel_guard': 'Decision/control', '/course_evidence_collector': 'Infrastructure', '/robot_state_publisher': 'Infrastructure', '/ros_gz_bridge': 'Simulation', '/rviz2': 'Visualization'}

## mission_1.node_vs_topic

A node is a program that performs a specific task, while a topic is a communication channel used by nodes to send and receive data

## mission_1.pipeline_roles

{'/course_cmd_vel_guard': 'Decide', '/course_evidence_collector': 'Support', '/robot_state_publisher': 'Support', '/ros_gz_bridge': 'Support', '/rviz2': 'Support'}

## mission_1.rviz_role

RViz is an observer because it visualizes information from the ROS system. Even though it publishes topics such as /clicked_point, /goal_pose, and /initialpose, it doesn't publish movement commands on /cmd_vel, so it is not directly controlling the robot. 

## mission_1.scan_observation

I found several +inf values in the range field, which represent directions where the LiDAR didn't detect an object within its min/max range. 

## mission_1.sense_decide_act

The LiDAR/simulator sense the environment and publishes gathered information on /scan. The command guard is part of decision because it processes movement commands and lastly the robot controller acts on the commands coming from /cmd_vel to move the robot

## mission_1.service_example

{'name': '/course_cmd_vel_guard/describe_parameters ', 'purpose': "It likely receives a request asking for information about the command guard's parameters and it responds with the descriptions of those parameters", 'type': 'rcl_interfaces/srv/DescribeParameters'}

## mission_1.service_vs_topic

A topic carries a stream of messages between publishers and subscribers, while a service uses a request and response system. A specific example from the lab would be /student_cmd_vel that carries velocity commands as a topic. On the other hand /course_cmd_vel_guard/get_parameters is a service that receives a request and returns a response 

## mission_1.teleop_change

When teleoperation starts 

## mission_1.tools_explanation

Gazebo is responsible for simulating the robot and its physical environment. It simulates things that would happen physically, like robot's location, how its wheels move, where the walls are, and more. While RViz is responsible for displaying ROS 2 data such as the robot's position and sensor readings. In other words, Gazebo simulates what is actually happening to the robot, while RViz shows us the information that ROS 2 has about the robot and world around it

## mission_1.topic_types

{'/odom': 'nav_msgs/msg/Odometry', '/scan': 'sensor_msgs/msg/LaserScan', '/student_cmd_vel': 'geometry_msgs/msg/Twist'}

## mission_2.measurement_explanation

For the curved trial, the estimated traveled path was 0.58 meters because it measures the distance the robot traveled along the curved path. The start-to-end distances was 0.524 meters because it measures a straight line between the robot's starting and ending points

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

For the straight trail, the live simulation result was very close to my prediction. I predicted that the robot would move 0.45 meters straight ahead, while in reality the estimated travel path was 0.433 meters and the direction change was 0 degrees

## mission_2.prediction_locks

{'straight': '2026-09-10T12:08:18.808776+00:00', 'rotation': '2026-09-10T12:13:50.519226+00:00', 'curve': '2026-09-10T12:20:39.152371+00:00', 'curve_modified': '2026-09-10T12:30:49.636951+00:00'}

## mission_2.predictions

{'straight': 'I predict the robot will finish 0.45 meters straight ahead of its starting point', 'rotation': 'I predict its position will remain the same while its direction will rotate to the left by 1.5 radians (so almost a 90 degree left turn in place)', 'curve': 'I predict the robot will follow a curved path to the right because it has a positive forward speed and a negative turning speed. It will travel 0.60 meters along the curve and turn 1.6 radians (about 92 degrees) to the right', 'curve_modified': 'This curve should be tighter and turn in the opposite direction (left) because its turn radius is approximately 0.20 meters compared with 0.38 meters for the first curve. In other words, the turning radius is smaller and the turning speed is positive instead of negative'}

## mission_2.safety_explanation

- The command guard checks that the commands given by the user are valid and safe to execute before sending them to the robot
- The final zero command tells the robot to stop at the end of the trial by setting both the forward and turning speeds to zero
- The timeout is needed if the program crashes or communication is lost because it stops the robot if it doesn't receive a new command within 0.5 seconds
 

## mission_3.data_to_command

The front_distance() function takes the list of LiDAR distances and finds the nearest valid distance in front of the robot. The decide_velocity() function then uses that distance to determine whether the robot should move forward or come to a stop depending on whether the obstacle is within the stop distance 

## mission_3.missing_data_safety

The robot stop when there is no valid front measurement instead of treating the path as clear because without a valid measurement, there is no way for it to know whether the path ahead is actually clear. Stopping is safer than assuming there is no obstacle and possibly causing the robot to crash 

## mission_3.system_layers

My decision functions use the LiDAR readings to determine whether the robot should move or stop. The supplied ROS node receives the /scan data, calls my functions, and publishes the resulting command to /student_cmd_vel. The command guard checks that command to make sure it is valid and safe before publishing it to /cmd_vel, which controls the robot

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}

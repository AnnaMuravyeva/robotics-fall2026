# Mission 2

## Predictions

{'straight': 'I predict the robot will finish 0.45 meters straight ahead of its starting point', 'rotation': 'I predict its position will remain the same while its direction will rotate to the left by 1.5 radians (so almost a 90 degree left turn in place)', 'curve': 'I predict the robot will follow a curved path to the right because it has a positive forward speed and a negative turning speed. It will travel 0.60 meters along the curve and turn 1.6 radians (about 92 degrees) to the right', 'curve_modified': 'This curve should be tighter and turn in the opposite direction (left) because its turn radius is approximately 0.20 meters compared with 0.38 meters for the first curve. In other words, the turning radius is smaller and the turning speed is positive instead of negative'}

## Prediction Locks

{'straight': '2026-09-10T12:08:18.808776+00:00', 'rotation': '2026-09-10T12:13:50.519226+00:00', 'curve': '2026-09-10T12:20:39.152371+00:00', 'curve_modified': '2026-09-10T12:30:49.636951+00:00'}

## Motion Comparison

For the straight trail, the live simulation result was very close to my prediction. I predicted that the robot would move 0.45 meters straight ahead, while in reality the estimated travel path was 0.433 meters and the direction change was 0 degrees

## Measurement Explanation

For the curved trial, the estimated traveled path was 0.58 meters because it measures the distance the robot traveled along the curved path. The start-to-end distances was 0.524 meters because it measures a straight line between the robot's starting and ending points

## Safety Explanation

- The command guard checks that the commands given by the user are valid and safe to execute before sending them to the robot
- The final zero command tells the robot to stop at the end of the trial by setting both the forward and turning speeds to zero
- The timeout is needed if the program crashes or communication is lost because it stops the robot if it doesn't receive a new command within 0.5 seconds
 

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

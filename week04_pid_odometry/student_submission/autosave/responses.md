# Autosaved responses

- Name: Anna Muravyeva
- Student ID: 24462672
- Section: (not provided)

## Check-in answers

### m3_prediction

Increasing speed may increase tracking error because there will be less time for a robot to correct its path. Too little derivative control may lead to overshooting or oscillation. Therefore, clearance from pedestrians may decrease, making the robot less safe.

### m3_technical

I predicted that increasing speed or using too little derivative control could increase tracking error and decrease pedestrian clearance.  The robot computes the direction it needs to move to reach the next route point and compares it to the direction it thinks it's facing. The PID uses this difference to adjust the steering and help robot stay on the right path. The green and orange paths showed very little separation, to the point that I didn't even realize there was an orange line to begin with, meaning that the wheel radius estimate was close to correct. If the wheel radius estimate was wrong then the robot would estimate its current position incorrectly and it could end up following the wrong path.

### m3_human

The consequential failure is the robot getting too close to or hitting a pedestrian because the robot couldn't follow its planned path. I would require more clearance from pedestrians and set a lower speed, even if it ends up making the robot take longer to reach its target. Responsibility belongs to the engineers and team responsible for the deployment of the robot as they need to test and make sure the settings are safe before the robot is allowed around people.

## Mission explanations

### mission_3

**technical_analysis**: I predicted that increasing speed or using too little derivative control could increase tracking error and decrease pedestrian clearance.  The robot computes the direction it needs to move to reach the next route point and compares it to the direction it thinks it's facing. The PID uses this difference to adjust the steering and help robot stay on the right path. The green and orange paths showed very little separation, to the point that I didn't even realize there was an orange line to begin with, meaning that the wheel radius estimate was close to correct. If the wheel radius estimate was wrong then the robot would estimate its current position incorrectly and it could end up following the wrong path.

**human_centered_analysis**: The consequential failure is the robot getting too close to or hitting a pedestrian because the robot couldn't follow its planned path. I would require more clearance from pedestrians and set a lower speed, even if it ends up making the robot take longer to reach its target. Responsibility belongs to the engineers and team responsible for the deployment of the robot as they need to test and make sure the settings are safe before the robot is allowed around people.

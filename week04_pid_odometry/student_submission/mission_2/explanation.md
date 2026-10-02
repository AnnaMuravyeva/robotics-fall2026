# mission_2 Submission

- Name: Anna Muravyeva
- Section: (not provided)

## Explanations

### prediction

The estimated forward distance will be too large in comparison to the actual distance traveled, while sideways distance will be smaller than the actual distance traveled.

### calibration_analysis

I predicted that if the forward pod scale was too large, the estimated forward distance would be too large. If the strafe pod scale was too small, the estimated sideways distance would be too small. The forward scale changed how much forward distance the odometry estimated. As the scale increased, the estimated distance became larger too. The strafe scale changed how much sideways distance the odometry estimated. As the scale increased, the estimated sideways distance became larger too. The sideways pod is needed because the robot can move sideways, but the forward pod can't measure this movement. Remaining drift can occur because the conversion from encoder ticks into physical distance isn't perfect and so small measurement errors can still build up over time.
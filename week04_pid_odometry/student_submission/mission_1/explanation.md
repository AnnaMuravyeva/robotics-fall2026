# mission_1 Submission

- Name: Anna Muravyeva
- Section: (not provided)

## Explanations

### prediction

With too little Kp, I expect it to move too slowly or struggle to reach its target because not enough correction is being applied. With too little Kd, I expect it to overshoot its target because it won't slow down its motion fast enough.

### tuning_analysis

I predicted that too little Kp would cause undershooting and too little Kd would cause overshooting. I changed Kp and Kd individually, setting each one equal to zero under initially tuned settings. I found that with Kp at zero, the arm moved around slowly and struggled to reach its target. The reason it moved at all is because Ki was still accumulating the error and attempting to correct it. With Kd at zero, the arm kept oscillating around the target. The hold phase showed the importance of balanced values, as they helped the arm settle closer to its target. Gravity compensation helped make some of the less ideal settings, such as stiff, preform well and settle close to the target.
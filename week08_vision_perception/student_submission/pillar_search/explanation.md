# pillar_search

## diagnosis
In my first attempt, the robot successfully centered the blue pillar. The camera showed the blue pillar and the mask was able to correctly identify its color. The centroid was initially to the left of the image center which gave a negative error, so the robot turned left until the error was close to zero. For my second attempt, I only changed the sequence to all four color and I kept the other settings the same. The robot completed both of my attempts successfully and the average image error went down slightly from 0.388 to 0.364.

## evidence
In my four-color attempt, all of the four colors were centered. The state timeline showed the robot searching, turning toward each pillar, and moving to the next color after centering. The camera images and masks showed that the robot was able to correctly detect the colored regions. The error graph showed the error getting closer to zero for each color. With that being said, centering a colored region does not prove that the robot recognizes the actual object or knows how far away it is. It only detects the color and its position in the image.

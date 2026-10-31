# Lab 7 saved answers

## line_following.comparison
In my practice attempt, I used a steering gain of 0.08. The camera mask was able to detect the magenta line and the robot followed it without losing it. I then tested the full track with the same gain and completed it in 187.15 seconds. On the curved sections, the error graph showed the robot moving from side to side as it tried to stay centered. The angular velocity graph showed the robot turning left and right to follow the curves. I then increased the steering gain to 0.15 and it helped the robot respond to curves faster. The completion time went down to 155.38 seconds and the average image error went down from 0.485 to 0.308. With that being said, both track attempts had zero line loss events which means that the higher gain improved tracking without causing our robot to lose the line.

## line_following.limits
In my first track attempt, the robot completed the track but it struggled to stay centered during curves. The error graph showed large changes which means that the steering gain of 0.08 was too weak for some turns. This was more of a control issue rather than an image processing problem since the robot was still able to detect the line.  After increasing it to 0.15, the robot was able to follow the line more closely and finish the track faster. Neither attempt lost the line, but this doesn't mean that the robot would be safe in a real world. A delivery robot would need additional sensors, like LiDAR or depth cameras, to detect people and obstacles. We should also test the robot around moving people, sudden obstacles, and different lighting conditions (day/nighttime) to make sure it is able to come to a safe stop.

## mission_1.diagnosis
In normal_1, the detector was able to correctly find the mug. The mask highlighted the mug and its handle, and the green box was placed around it. In dim_1, the detector failed to identify the mug, it selected the edge of what appears to be a separate trackpad (I am not sure) instead. The darker lighting changed which pixels passed my brightness limit of 80.  As a result, the detect chose contour 4 because it passed the minimum area and circularity requirements, even though it wasn't the mug. 

## mission_1.limitations
During practice, I lowered the maximum brightness from 180 to 80. This helped to remove some of the desk from the mask and made the selected box fit the mug better. In an attempt to remove even more of the desk, I tried lowering it to 60, but parts of the hand started disappearing, so I kept it at 80. One limitation is that the detector only looks at colors and shapes, so it could potentially struggle with a different colored mug or a background that has similar colors.

## mission_2.choice
I would recommend learned detector with a threshold of 0.40 because even though, similarly to the classified detector, it failed to locate mugs in dim and occluded images, it didn't produce false boxes. With that being said, it was slower (19-20 ms per image compare to 1-2 ms for classical). I would also test a lower threshold of 0.20 to see if it helps to detect more mugs. For normal_1, the foreground mask had an IoU of 0.5756 and a Dice score of 0.7306. Even though, it got most of the mug, it also included unwanted areas and missed some parts. A detailed mask alone can't identify which object is the mug. One limitation is the small number of test images, so we would need to do more testing before using either one of the detectors on an actual robot.

## mission_2.comparison
Under normal conditions, both detectors were able to find 2 mugs correctly, with 0 false boxes and 0 missed mugs. Under dim conditions, both detectors had 0 correct boxes and missed 2  mugs,  but the classical detector produced 1 false box, while the learned detector didn't. Under occluded conditions, both detectors once again had 0 correct boxes and missed 2 mugs, but the classical detector produced 2 false boxes, while the learned detector didn't. These differences are important because false boxes could cause our robot to grab the wrong object. For example, in dim_1, the classical detector incorrectly placed a box around the trackpad, while the learned detector didn't produce any box. With that being said, both detectors failed to locate the mug.

## pillar_search.diagnosis
In my first attempt, the robot successfully centered the blue pillar. The camera showed the blue pillar and the mask was able to correctly identify its color. The centroid was initially to the left of the image center which gave a negative error, so the robot turned left until the error was close to zero. For my second attempt, I only changed the sequence to all four color and I kept the other settings the same. The robot completed both of my attempts successfully and the average image error went down slightly from 0.388 to 0.364.

## pillar_search.evidence
In my four-color attempt, all of the four colors were centered. The state timeline showed the robot searching, turning toward each pillar, and moving to the next color after centering. The camera images and masks showed that the robot was able to correctly detect the colored regions. The error graph showed the error getting closer to zero for each color. With that being said, centering a colored region does not prove that the robot recognizes the actual object or knows how far away it is. It only detects the color and its position in the image.

## final.synthesis
This lab showed me that getting a robot to recognize something through its camera is only the first step. In Mission 1, both the classical and learned detectors were able to correctly detect mugs under normal lighting, but that wasn't the case in dim lighting and when the mugs were partially covered as both detectors missed the mugs. However, unlike learned detector, classical detector made more false detections. Therefore, I think the learned detector was more reliable, but neither worked well in difficult conditions.

In Mission 2, the robot was able to successfully center all four pillars in the four color sequence. The camera mask helped our robot find each color and the robot turned until the detection region was near the center of the image. With that being said, this only showed us that it could center a colored region, not that it knew what the object was or distance to it. 

In Mission 3, I tested how well a robot can follow the path with two different steering gains. With a gain of 0.08, the robot completed the track in 187.15 seconds with an average image error of 0.485. After I increased the gain to 0.15, it finished in 155.38 seconds, and the error went down to 0.308. Neither one of the attempts lost the line.

Overall, these mission taught me that completion of a task doesn't equal to safety. Camera detection can fail under different conditions and the robot needs additional sensing and testing before it could safely operate in the real world

## final.course_reflection
In this lab, I enjoyed seeing how the robot used its camera to recognize different colors and respond to them. It made me realize how much testing and adjusting goes into making even simple tasks work properly. This activity  also once again reminded me that getting a robot to complete a task is one thing, but making sure it can do so safely around obstacles and people is the most important and, at the same time, difficult part

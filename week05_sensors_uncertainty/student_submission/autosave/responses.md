# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI 39536
- email: anna.muravyeva72@login.cuny.edu
- name: Anna Muravyeva

## concepts.observation

When I increased the noise, the readings became more scattered around the true value. The standard deviation increased, meaning that the measurements weren't as consistent. When I increased the bias, the reading shifted away from the true value. The mean increased even though the readings were still grouped close to each other. 

## final.course_reflection

This activity made me realize how much even small changes in settings can impact a robot's behavior. What stood out to me was that changing one parameter doesn't always result in the way we expected it to. For example, when I increased the caution margin for the warehouse robot, the detection delay improved, but the false-safe and unnecessary stop rates didn't change. Overall, I found this lab interesting, but I have to admit  that it was somewhat difficult in the beginning, as we had to do quite a bit of math, and it took me some time to understand the formulas.

## final.synthesis

One of the main things I learned from this lab is that a robot's ability to make safe decision depends on more than just its sensors. In Mission 1, we calculated different statistics from a sensor dataset and looked at missing readings and outliers. For example, most of the measurements were close to 2 meters, but there was one unusually low reading. This mission showed why it's important to understand how reliable the measurements are before we use them to make decisions.

In Mission 2, we tested different filters, window sizes, and sensor weights to see how they affected the accuracy of our measurements. For example, when I increased the moving average windows from 3 to 11, the RMSE increased. The best result I got was with the median filter, a window of 3, and a sensor A weight of 0.50, which gave an RMSE of 0.1270. This mission showed that smoother measurements don't always equal to better results.

In Mission 3, we applied the ideas from the other two missions to warehouse and assistive robots. Both of my final configurations passed all seven required tests. However, I set a higher stopping threshold for the assistive robot compared to the warehouse robot because of the difference in the environment they each operate in. This  mission showed why we need to consider not only the sensor readings and filtering methods, but also where the robot operates and how its decisions could impact people 

## mission_1.bias

-0.014

## mission_1.bias_vs_variance

My prediction was mostly correct. The mean was 1.99 m, which is very close to the true distance of 2.00 m. The bias and variance were both low. This means that most readings were consistent and close to the true value. With that being said, I did notice an outlier that was much lower than the other readings. Most readings were also rounded to the same two values, 1.90 m or 2.00 m. Bias describes how far the average is from the true value, while variance describes how scattered the readings are.

## mission_1.dropouts

6

## mission_1.mean

1.99

## mission_1.median

2.00

## mission_1.more_samples

No, I don't think more samples would remove this sensor's main problem because the sensor rounds its readings to certain values. Most of the readings were either 1.90 m or 2.00 m. So even with more sample, the sensor would still round them. More sample can help with getting a better average, but the rounding issue would stay.

## mission_1.outliers

1

## mission_1.prediction

I predict that a consistently biased sensor would have readings grouped around a value that is different from the true distance of  2.00 m. Therefore, the mean would be far from the true value, the bias would be high, and variance would be low. On the other hand, a noisy sensor would have readings scattered around the true value. The mean would probably be close to 2.00 m,  the bias would be low, and the variance would be high.

## mission_1.prediction_draft

I predict that a consistently biased sensor would have readings grouped around a value that is different from the true distance of  2.00 m. Therefore, the mean would be far from the true value, the bias would be high, and variance would be low. On the other hand, a noisy sensor would have readings scattered around the true value. The mean would probably be close to 2.00 m,  the bias would be low, and the variance would be high.

## mission_1.profile

quantized

## mission_1.robot_consequence

One robot decision this imperfection could change is the robot's decision to slow down or stop when a person is on its way. Since the distance is being rounded, the robot might not notice small changes in how close the person is. This could lead to a collision as the robot might not react in time. 

## mission_1.variance

0.004

## mission_2.comparison

When comparing the 3 moving average windows, I noticed that the error increased as the window size increased. With a window of 3, the RMSE was 0.1395, with 7 it increase to 0.1504, and with 11 it increased to 0.1601. With that being said, the response delay stayed the same at 1.1 seconds for all of the windows. When comparing the median filter and moving average with a window of 3, the median filter had a slightly lower RMSE of 0.1389 compared to 0.1395. The response delay was the same for both at 1.1 seconds. This means that the median filter was slightly more accurate in this case.

## mission_2.fusion_choice

When comparing the 3 weights, I noticed that when we increased the weight from 0.25 to 0.50, the RMSE went down from 0.1389 to 0.1270. The response delay also decreased from 1.1 to 0.9 seconds. With that being said, when we increased the weight even more to 0.75, the RMSE increased to 0.1335, while the response delay decreased to 0.45 seconds. I would choose a weight of 0.50 because it had the lowest RMSE and a pretty reasonable response delay. Sensor A is fast but noisy, while Sensor B is more consistent but biased. With a weight of 0.50, we are relying on both sensors equally, which gives us a good balance between accuracy and response time. 

## mission_2.manual_average

4.1667

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

I predict that increasing the weight from 0.50 to 0.75 will most likely reduce the error even more because we are relying even less on the biased sensor.  However, the readings might become noisier as we are giving more weight to the noisier sensor.  The response delay will probably decrease slightly or stay the same.

## mission_2.responsiveness

Smoothing helps to reduce noise in the readings, but it can also make our robot slower when it comes to reacting to changes in distance. In the experiment, all 3 moving average windows had the same response delay of 1.1 seconds. However, when we increased the weight from 0.25 to 0.50, the delay decreased to 0.9 seconds, and with a weight of 0.75, it decreased even more to 0.45 seconds. This shows that when we give more weight to the faster sensor, the robot responds faster. For a person nearby, a longer response delay could be dangerous as the robot might not notice them getting closer and might not be able to stop in time.

## mission_2.selected

4

## mission_3.Assistive.prediction_draft

I predict that decreasing the caution margin from 0.20 m to 0.10 m will make the robot less cautious, as it will start slowing down or stopping at a shorter distance. But, I expect that this could help to reduce the number of unnecessary stops, making the robot more convenient for those who rely on it. With that being said, the false-safe rate and response delay could potentially increase because there is less room to react when someone approaches quickly.

## mission_3.Warehouse.prediction_draft

I predict that increasing the caution margin from 0.10 m to 0.20 m will make our robot more cautious because it will start slowing down or stopping at a greater distance. I expect to see the false-safe rate decrease as the robot will have more room to react. With that being said, this could also lead to an increased number of unnecessary stops, therefore slowing down the work in the warehouse. The response delay will probably stay the same or decrease because the robot will start taking precautions earlier.

## mission_3.context_comparison

For the warehouse robot, I would choose a stopping threshold of 0.75 m with a caution margin of 0.20 m. For the assistive robot, I would choose a stopping threshold of 0.95 m with a caution margin of 0.20 m. The assistive robot needs a higher stopping threshold because it operates closely around people who may potentially have limited mobility. The warehouse robot had a false-safe rate of 0.62 percent and a detection delay of 0 seconds, while the assistive robot had a false-safe rate of 0 percent and a delay of 0.05 seconds. Both configurations passed all seven required tests, but I think safety is especially important for the assistive robot because people directly rely on it.

## mission_3.error_costs

In the warehouse, false-safe decisions could put workers at risk, while unnecessary stops could slow down work. In both configurations, the false-safe rate stayed at 0.62 percent, and the unnecessary stop rate stayed at 5.61 percent. However, the detection delay decreased from 0.10 to 0 seconds when I increased the caution margin. For the assistive robot, false-safe decisions could put people with limited mobility in danger, while unnecessary stops could make the robot less convenient. Both configurations had a false-safe rate of 0 percent and an unnecessary stop rate of 1.35 percent. But, the detection delay went up from 0.05 to 0.20 seconds when I decreased the caution margin.

## mission_3.limitations

The seven tests show that both robots can handle different situations such as missing readings, conflicting sensors, and more. However, passing these tests doesn't mean that the robots are completely safe to use in real life, where situations can be more unpredictable. Before deployment, I would gather feedback from target audiences, to better understand their needs and concerns. I would also test both robots in crowded environments with people moving at different speeds to see how they perform in more complicated situations.

# Mission 2

## comparison

When comparing the 3 moving average windows, I noticed that the error increased as the window size increased. With a window of 3, the RMSE was 0.1395, with 7 it increase to 0.1504, and with 11 it increased to 0.1601. With that being said, the response delay stayed the same at 1.1 seconds for all of the windows. When comparing the median filter and moving average with a window of 3, the median filter had a slightly lower RMSE of 0.1389 compared to 0.1395. The response delay was the same for both at 1.1 seconds. This means that the median filter was slightly more accurate in this case.

## fusion_choice

When comparing the 3 weights, I noticed that when we increased the weight from 0.25 to 0.50, the RMSE went down from 0.1389 to 0.1270. The response delay also decreased from 1.1 to 0.9 seconds. With that being said, when we increased the weight even more to 0.75, the RMSE increased to 0.1335, while the response delay decreased to 0.45 seconds. I would choose a weight of 0.50 because it had the lowest RMSE and a pretty reasonable response delay. Sensor A is fast but noisy, while Sensor B is more consistent but biased. With a weight of 0.50, we are relying on both sensors equally, which gives us a good balance between accuracy and response time. 

## manual_average

4.1667

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

I predict that increasing the weight from 0.50 to 0.75 will most likely reduce the error even more because we are relying even less on the biased sensor.  However, the readings might become noisier as we are giving more weight to the noisier sensor.  The response delay will probably decrease slightly or stay the same.

## responsiveness

Smoothing helps to reduce noise in the readings, but it can also make our robot slower when it comes to reacting to changes in distance. In the experiment, all 3 moving average windows had the same response delay of 1.1 seconds. However, when we increased the weight from 0.25 to 0.50, the delay decreased to 0.9 seconds, and with a weight of 0.75, it decreased even more to 0.45 seconds. This shows that when we give more weight to the faster sensor, the robot responds faster. For a person nearby, a longer response delay could be dangerous as the robot might not notice them getting closer and might not be able to stop in time.

## selected

4

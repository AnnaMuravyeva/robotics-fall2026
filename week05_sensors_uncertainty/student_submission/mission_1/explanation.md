# Mission 1

## bias

-0.014

## bias_vs_variance

My prediction was mostly correct. The mean was 1.99 m, which is very close to the true distance of 2.00 m. The bias and variance were both low. This means that most readings were consistent and close to the true value. With that being said, I did notice an outlier that was much lower than the other readings. Most readings were also rounded to the same two values, 1.90 m or 2.00 m. Bias describes how far the average is from the true value, while variance describes how scattered the readings are.

## dropouts

6

## mean

1.99

## median

2.00

## more_samples

No, I don't think more samples would remove this sensor's main problem because the sensor rounds its readings to certain values. Most of the readings were either 1.90 m or 2.00 m. So even with more sample, the sensor would still round them. More sample can help with getting a better average, but the rounding issue would stay.

## outliers

1

## prediction

I predict that a consistently biased sensor would have readings grouped around a value that is different from the true distance of  2.00 m. Therefore, the mean would be far from the true value, the bias would be high, and variance would be low. On the other hand, a noisy sensor would have readings scattered around the true value. The mean would probably be close to 2.00 m,  the bias would be low, and the variance would be high.

## prediction_draft

I predict that a consistently biased sensor would have readings grouped around a value that is different from the true distance of  2.00 m. Therefore, the mean would be far from the true value, the bias would be high, and variance would be low. On the other hand, a noisy sensor would have readings scattered around the true value. The mean would probably be close to 2.00 m,  the bias would be low, and the variance would be high.

## profile

quantized

## robot_consequence

One robot decision this imperfection could change is the robot's decision to slow down or stop when a person is on its way. Since the distance is being rounded, the robot might not notice small changes in how close the person is. This could lead to a collision as the robot might not react in time. 

## variance

0.004

# Mission 3

## Assistive.prediction_draft

I predict that decreasing the caution margin from 0.20 m to 0.10 m will make the robot less cautious, as it will start slowing down or stopping at a shorter distance. But, I expect that this could help to reduce the number of unnecessary stops, making the robot more convenient for those who rely on it. With that being said, the false-safe rate and response delay could potentially increase because there is less room to react when someone approaches quickly.

## Warehouse.prediction_draft

I predict that increasing the caution margin from 0.10 m to 0.20 m will make our robot more cautious because it will start slowing down or stopping at a greater distance. I expect to see the false-safe rate decrease as the robot will have more room to react. With that being said, this could also lead to an increased number of unnecessary stops, therefore slowing down the work in the warehouse. The response delay will probably stay the same or decrease because the robot will start taking precautions earlier.

## context_comparison

For the warehouse robot, I would choose a stopping threshold of 0.75 m with a caution margin of 0.20 m. For the assistive robot, I would choose a stopping threshold of 0.95 m with a caution margin of 0.20 m. The assistive robot needs a higher stopping threshold because it operates closely around people who may potentially have limited mobility. The warehouse robot had a false-safe rate of 0.62 percent and a detection delay of 0 seconds, while the assistive robot had a false-safe rate of 0 percent and a delay of 0.05 seconds. Both configurations passed all seven required tests, but I think safety is especially important for the assistive robot because people directly rely on it.

## error_costs

In the warehouse, false-safe decisions could put workers at risk, while unnecessary stops could slow down work. In both configurations, the false-safe rate stayed at 0.62 percent, and the unnecessary stop rate stayed at 5.61 percent. However, the detection delay decreased from 0.10 to 0 seconds when I increased the caution margin. For the assistive robot, false-safe decisions could put people with limited mobility in danger, while unnecessary stops could make the robot less convenient. Both configurations had a false-safe rate of 0 percent and an unnecessary stop rate of 1.35 percent. But, the detection delay went up from 0.05 to 0.20 seconds when I decreased the caution margin.

## limitations

The seven tests show that both robots can handle different situations such as missing readings, conflicting sensors, and more. However, passing these tests doesn't mean that the robots are completely safe to use in real life, where situations can be more unpredictable. Before deployment, I would gather feedback from target audiences, to better understand their needs and concerns. I would also test both robots in crowded environments with people moving at different speeds to see how they perform in more complicated situations.

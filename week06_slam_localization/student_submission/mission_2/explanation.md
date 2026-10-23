# Mission 2

## Comparison

My first route took 20 minutes, while my second route took 94 minutes. Even though the second route took a lot longer to complete, it did result in a better map overall. The known area went up from 115.9 m^2 to 147.38 m^2. Also, the quality score improved quite significantly, it went up from 47.1 to 73.9. The speckle fraction decreased from 10.61% to 6.58%. All of this partially supports my initial prediction that exploring the perimeter of each room and making multiple passes through the same area would help create a better map. With that being said, it took me almost five times as long to explore the second route compared to the first. The first route was a lot more efficient, covering 5.8 m^2 per minute compared to only 1.57 m^2 per minute during the second route. So overall, the second strategy did produce better coverage, but it required a lot more time to do so. Also, some of the walls were still misaligned, even though I went through that area about 5 times in an attempt to fix them.

## Map Choice

Out of the two maps, I would definitely trust the second map more because it shows more of the house, and the outlines of several rooms are easier to recognize. With that being said, it still has areas, especially on the right side of the house, where the walls overlap or  appear duplicated. I went over that area about 5 times, hoping that SLAM would correct the alignment issues, but the walls only became more distorted. The duplicated fragment only appeared after I decided to go over the area again to fix some alignment issues. This shows that revisiting an area doesn't guarantee an improvement. One limitation of these images and measurements is that even though the second map has a higher quality score, it doesn't really mean that the walls are in their correct positions. We would need to look at the actual layout of the house to know if our map is truly accurate.

## Strategy.Original Prediction

For my second route, I want to explore the perimeter of each room instead just entering and exiting the room. I also plan to return to areas I have already explored instead of passing through them only once, to give SLAM a chance to correct any drift. I think this new strategy might help create a clearer map with less overlapping walls and unexplored areas. With that being said, it will take longer because I will be exploring each room more carefully and I will be making a second pass.

## Strategy.Prediction Draft

For my second route, I want to explore the perimeter of each room instead just entering and exiting the room. I also plan to return to areas I have already explored instead of passing through them only once, to give SLAM a chance to correct any drift. I think this new strategy might help create a clearer map with less overlapping walls and unexplored areas. With that being said, it will take longer because I will be exploring each room more carefully and I will be making a second pass.

# mission_1

## diagnosis
In normal_1, the detector was able to correctly find the mug. The mask highlighted the mug and its handle, and the green box was placed around it. In dim_1, the detector failed to identify the mug, it selected the edge of what appears to be a separate trackpad (I am not sure) instead. The darker lighting changed which pixels passed my brightness limit of 80.  As a result, the detect chose contour 4 because it passed the minimum area and circularity requirements, even though it wasn't the mug. 

## limitations
During practice, I lowered the maximum brightness from 180 to 80. This helped to remove some of the desk from the mask and made the selected box fit the mug better. In an attempt to remove even more of the desk, I tried lowering it to 60, but parts of the hand started disappearing, so I kept it at 80. One limitation is that the detector only looks at colors and shapes, so it could potentially struggle with a different colored mug or a background that has similar colors.

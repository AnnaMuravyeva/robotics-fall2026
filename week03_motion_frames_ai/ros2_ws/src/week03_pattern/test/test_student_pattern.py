import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        
        self.assertEqual(len(segments), 8) #Checking the number of segments
        for i in range(0, len(segments), 4):
            self.assertAlmostEqual(segments[i].linear_x * segments[i].duration, 0.40) #Checking the distance covered by the straight segments
            self.assertAlmostEqual(segments[i+2].linear_x * segments[i+2].duration, 0.25) #Checking the distance covered by the short straight segments 

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        #Checking that the pattern switches between straight and arc segments
        for i in range(len(segments)):
            if i % 2 == 0:
                self.assertAlmostEqual(segments[i].angular_z, 0.0) #Straight segment should have zero angular velocity
            else:
                self.assertGreater(segments[i].angular_z, 0.0) #Arc segment should turn left with positive angular velocity
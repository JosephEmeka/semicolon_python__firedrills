import unittest

import seven_segment
from seven_segment import SevenSegment


class Test_SevenSegmentDisplayTests(unittest.TestCase):
    def test_binary_(self):
        my_display = SevenSegment('11111101')
        self.assertIsInstance(my_display, seven_segment.SevenSegment)

import unittest
from src.defineRectangles import defineRectangles

class test_defineRectangles(unittest.TestCase):

    def test_lowerLimitLengthCheck(self):
        rectangles = defineRectangles(3)
        self.assertEqual(3, len(rectangles))
    
    def test_upperLimitLengthCheck(self):
        rectangles = defineRectangles(10)
        self.assertEqual(10, len(rectangles))
    
    def test_maxLimitCheck(self):
        rectangles = defineRectangles(11)
        self.assertEqual(rectangles, -1)

    def test_otherDataTypeCheck(self):
        rectangles = defineRectangles("nonsense")
        self.assertEqual(rectangles, -1)
    
    def test_minLimitCheck(self):
        rectangles = defineRectangles(0)
        self.assertEqual(rectangles, -1)
    
    def test_negativeValueCheck(self):
        rectangles = defineRectangles(-4)
        self.assertEqual(rectangles, -1)
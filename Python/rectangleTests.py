import unittest
from Rectangle import *

# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def test1(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
    
    def test2(self):
        rectangle = Rectangle(5, 0)
        self.assertEqual(rectangle.get_area(), 0, "incorrect area")
 
# Run the test
unittest.main()
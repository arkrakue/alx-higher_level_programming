import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Method to set up test cases"""
        pass

    def test_width(self):
        """Test for width attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(8, 7)
        self.assertEqual(r2.width, 8)

    def test_height(self):
        """Test for height attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(8, 7)
        self.assertEqual(r2.height, 7)

    def test_x(self):
        """Test for x attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(8, 7, 5)
        self.assertEqual(r2.x, 5)

    def test_y(self):
        """Test for y attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(8, 7, 5, 9)
        self.assertEqual(r2.y, 9)

    def test_area(self):
        """Test for area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        """Test for display method"""
        pass

    def test_str(self):
        """Test for __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

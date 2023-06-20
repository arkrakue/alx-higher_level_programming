import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Method to set up test cases"""
        pass

    def test_size(self):
        """Test for size attribute"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(7)
        self.assertEqual(s2.size, 7)

    def test_x(self):
        """Test for x attribute"""
        s1 = Square(5)
        self.assertEqual(s1.x, 0)
        s2 = Square(7, 4)
        self.assertEqual(s2.x, 4)

    def test_y(self):
        """Test for y attribute"""
        s1 = Square(5)
        self.assertEqual(s1.y, 0)
        s2 = Square(7, 4, 3)
        self.assertEqual(s2.y, 3)

    def test_area(self):
        """Test for area method"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(7, 0, 0, 12)
        self.assertEqual(s2.area(), 49)

    def test_display(self):
        """Test for display method"""
        pass

    def test_str(self):
        """Test for __str__ method"""
        s1 = Square(5, 0, 0, 12)
        self.assertEqual(str(s1), '[Square] (12) 0/0 - 5')

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_width_setter(self):
        r1 = Rectangle(10, 2)
        r1.width = 5
        self.assertEqual(r1.width, 5)

    def test_height_setter(self):
        r1 = Rectangle(10, 2)
        r1.height = 7
        self.assertEqual(r1.height, 7)

    def test_x_setter(self):
        r1 = Rectangle(10, 2)
        r1.x = 3
        self.assertEqual(r1.x, 3)

    def test_y_setter(self):
        r1 = Rectangle(10, 2)
        r1.y = 4
        self.assertEqual(r1.y, 4)

if __name__ == '__main__':
    unittest.main()

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rectangle = Rectangle(10, 2)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

        rectangle = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.id, 12)

    def test_area(self):
        rectangle = Rectangle(10, 2)
        self.assertEqual(rectangle.area(), 20)

if __name__ == '__main__':
    unittest.main()


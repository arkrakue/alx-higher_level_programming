import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(10)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square = Square(10, 4, 5, 12)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)
        self.assertEqual(square.id, 12)

    def test_area(self):
        square = Square(10)
        self.assertEqual(square.area(), 100)


if __name__ == '__main__':
    unittest.main()

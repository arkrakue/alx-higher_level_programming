import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        base = Base()
        self.assertEqual(base.id, 1)

        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_to_json_string(self):
        base = Base()
        dictionary = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]')


if __name__ == '__main__':
    unittest.main()

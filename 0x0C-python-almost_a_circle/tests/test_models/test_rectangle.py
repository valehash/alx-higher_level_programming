import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_id(self):
        r1 = Rectangle(10, 2, 4, 5, 12)
        width = r1.width

        self.assertEqual(r1.id, 12)
        self.assertEqual(width, 10)

if __name__ == "__main__":
    unittest.main()

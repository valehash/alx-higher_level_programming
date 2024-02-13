import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

	def test_id(self):
        	r1 = Rectangle(10, 2, 4, 5, 12)

        	width = r1.get_width()

        	self.assertEqual(r1.id, 12)

if __name__ == "__main__":
	unittest.main()

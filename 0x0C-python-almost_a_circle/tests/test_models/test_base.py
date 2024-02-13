import unittest
from models.base import Base

class  TestBase(unittest.TestCase):

	def test_id(self):
		b1 = Base()
		id = b1.id
		self.assertEqual(id, 1)

if __name__ == "__main__":
	unittest.main()

import unittest
import app


class TestMain(unittest.TestCase):

	def test_case_one(self):
		text = '()[]{}(([])){[()][]}'
		result = app.check(text)
		self.assertEqual(result,True)

	def test_case_two(self):
		text = '())[]{}'
		result = app.check(text)
		self.assertEqual(result,False)	
		
	def test_case_three(self):
		text = '[(])'
		result = app.check(text)
		self.assertEqual(result,True)

if __name__ == '__main__':
	unittest.main()
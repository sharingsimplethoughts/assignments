import unittest
import app


class TestMain(unittest.TestCase):

	def test_case_one(self):
		co = app.CheckOut(app.pricingService)
		co.scan('1')
		co.scan('1')
		co.scan('1')
		co.scan('4')
		co.scan('1')
		co.scan('2')
		co.scan('2')
		co.scan('2')
		result = co.calculate_my_order_detail()
		self.assertEqual(result,100.00)

	def test_case_two(self):
		co = app.CheckOut(app.pricingService)
		co.scan('1')
		co.scan('2')
		co.scan('3')
		co.scan('4')
		co.scan('1')
		co.scan('2')
		co.scan('3')
		co.scan('4')
		result = co.calculate_my_order_detail()
		self.assertEqual(result,215.00)	
		
	def test_case_three(self):
		co = app.CheckOut(app.pricingService)
		co.scan('1')
		co.scan('3')
		co.scan('1')
		co.scan('3')
		co.scan('2')
		co.scan('4')
		co.scan('2')
		co.scan('2')
		result = co.calculate_my_order_detail()
		self.assertEqual(result,230.00)

if __name__ == '__main__':
	unittest.main()
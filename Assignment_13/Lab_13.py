import unittest
import math
import Grades

import os
os.system("cls")

######################################################################################

class Grade_Test(unittest.TestCase):

	def test_total_returns_total_of_list(self):
		result = Grades.total([1, 10, 22])	
		self.assertEqual(result,33, "The total function should return 33")


	def test_total_returns_0(self):
		result = Grades.total([]) # 0
		self.assertEqual(result,0, "The total function should return 0")

	def test_average_one(self):
		result = Grades.average([2, 5, 9]) # 5.3333333333333 not equal to 0.53333000000
		self.assertAlmostEqual(result, 5.3333, 2, "The average function should return 5.3333")
    

	def test_average_two(self):
		result = Grades.average([2, 15, 22, 9]) # 12
		self.assertAlmostEqual(result, 12, 4, "The average function should return 12")

	def test_average_returns_nan(self):
		result = Grades.average([]) # nan which represents Not A Number
		self.assertIs(math.nan, result, "The average function shoudl return ")

	def test_median(self):
		with self.assertRaises(ValueError):
			result = Grades.median([])

unittest.main()
# Run this test case from the parent directory using: python -m unittest tests.test_clumsy_factorial_solution.

import unittest
from src.clumsy_factorial_solution import ClumsyFactorialSolution

class ClumsyFactorialSolutionTestCase(unittest.TestCase):

	clumsyFactorialSolution = ClumsyFactorialSolution()

	def test_clumsy_4(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(4), 7)

	def test_clumsy_10(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(10), 12)

	def test_clumsy_1(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(1), 1)

	def test_clumsy_2(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(2), 2)

	def test_clumsy_3(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(3), 6)

if __name__ == '__main__':
	unittest.main()
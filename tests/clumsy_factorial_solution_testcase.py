import unittest
from src.clumsy_factorial_solution import ClumsyFactorialSolution

class ClumsyFactorialSolutionTestCase(unittest.TestCase):

	clumsyFactorialSolution = ClumsyFactorialSolution()

	def test_clumsy_4(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(4), 7)

	def test_clumsy_10(self):
		self.assertEqual(self.clumsyFactorialSolution.clumsy(10), 12)

if __name__ == '__main__':
	unittest.main()
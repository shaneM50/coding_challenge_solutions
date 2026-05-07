# Run this test case from the parent directory using: python -m unittest tests.FILE_NAME.

import unittest
import time
import random
from src.merge_sort_solution import MergeSortSolution

class MergeSortSolutionTestCase(unittest.TestCase):

	def setUp(self):
		self.merge_sort = MergeSortSolution()

	def test_merge_sort_already_sorted(self):
		data = ['a', 'b', 'c', 'd', 'e']
		expected = ['a', 'b', 'c', 'd', 'e']
		self.assertEqual(self.merge_sort.sortArray(data), expected)

	def test_merge_sort_reverse_ordered(self):
		data = ['z', 'y', 'x', 'w', 'v', 'u']
		expected = ['u', 'v', 'w', 'x', 'y', 'z']
		self.assertEqual(self.merge_sort.sortArray(data), expected)

	def test_merge_sort_with_duplicates(self):
		data = ['m', 'b', 'm', 'a', 'b', 'z', 'm']
		expected = ['a', 'b', 'b', 'm', 'm', 'm', 'z']
		self.assertEqual(self.merge_sort.sortArray(data), expected)

	def test_merge_sort_mixed_letters(self):
		data = ['h', 'a', 'z', 'd', 'q', 'b', 'y', 'e']
		expected = ['a', 'b', 'd', 'e', 'h', 'q', 'y', 'z']
		self.assertEqual(self.merge_sort.sortArray(data), expected)

	def test_merge_sort_short_odd_length(self):
		data = ['k', 'e', 'c', 'k', 'a']
		expected = ['a', 'c', 'e', 'k', 'k']
		self.assertEqual(self.merge_sort.sortArray(data), expected)

	def test_time_complexity_approximately_n_log_n(self):
		# This is a heuristic timing test, not a strict proof of complexity.
		# It checks that doubling n does not make the time explode worse than ~4x.
		n1 = 10_000
		n2 = 20_000

		# Use integers for performance
		data1 = [random.randint(0, 1_000_000) for _ in range(n1)]
		data2 = [random.randint(0, 1_000_000) for _ in range(n2)]

		start1 = time.perf_counter()
		self.merge_sort.sortArray(list(data1))
		t1 = time.perf_counter() - start1

		start2 = time.perf_counter()
		self.merge_sort.sortArray(list(data2))
		t2 = time.perf_counter() - start2

		# For O(n log n), going from n to 2n should increase time by ~2x–2.2x.
		# Allow some slack for noise: assert it's not worse than 4x.
		if t1 > 0:
			ratio = t2 / t1
			self.assertLessEqual(
				ratio,
				4.0,
				msg=f"Expected ~O(n log n), but 2n took {ratio:.2f}x longer than n"
			)


if __name__ == '__main__':
	unittest.main()
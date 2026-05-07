# Run this test case from the parent directory using: python -m unittest tests.FILE_NAME.

import unittest
import time
import random
from src.binary_search_solution import BinarySearchSolution

class BinarySearchSolutionTestCase(unittest.TestCase):

	def setUp(self):
		self.binary_search = BinarySearchSolution()

	def test_target_in_middle(self):
		nums = [1, 3, 5, 7, 9]
		target = 5
		self.assertEqual(self.binary_search.search(nums, target), 2)

	def test_target_at_beginning(self):
		nums = [1, 3, 5, 7, 9]
		target = 1
		self.assertEqual(self.binary_search.search(nums, target), 0)

	def test_target_at_end(self):
		nums = [1, 3, 5, 7, 9]
		target = 9
		self.assertEqual(self.binary_search.search(nums, target), 4)

	def test_target_not_present(self):
		nums = [1, 3, 5, 7, 9]
		target = 6
		self.assertEqual(self.binary_search.search(nums, target), -1)

	def test_single_element_found(self):
		nums = [10]
		target = 10
		self.assertEqual(self.binary_search.search(nums, target), 0)

	def test_single_element_not_found(self):
		nums = [10]
		target = -1
		self.assertEqual(self.binary_search.search(nums, target), -1)

	def test_empty_array(self):
		nums = []
		target = 1
		self.assertEqual(self.binary_search.search(nums, target), -1)

	def test_duplicates_target_present(self):
		# Depending on spec, any valid index of target is acceptable.
		nums = [2, 4, 4, 4, 8]
		target = 4
		index = self.binary_search.search(nums, target)
		self.assertIn(index, [1, 2, 3])

	def test_negative_numbers(self):
		nums = [-10, -5, -1, 0, 3, 8]
		target = -5
		self.assertEqual(self.binary_search.search(nums, target), 1)

	"""
	Heuristic timing test: for O(log n), increasing n a lot should not
	increase time by more than a small factor. Very loose check.
	
	For an O(log n) algorithm, t2 should be on the same order as t1, so ratio should be around 1, maybe a bit higher).
	"""
	def test_time_complexity_approximately_log_n(self):
		# Choose large n values so overhead is small relative to the search work.
		n1 = 1_000_000
		n2 = 16_000_000  # 16x bigger → log2 grows from ~20 to ~24 (≈20% increase)

		nums1 = list(range(n1))
		nums2 = list(range(n2))
		target1 = n1 - 1
		target2 = n2 - 1

		start1 = time.perf_counter()
		self.binary_search.search(nums1, target1)
		t1 = time.perf_counter() - start1

		start2 = time.perf_counter()
		self.binary_search.search(nums2, target2)
		t2 = time.perf_counter() - start2

		if t1 > 0:
			ratio = t2 / t1
			# For true O(log n), ratio should be close to 1; allow some slack (≤ 3x).
			self.assertLessEqual(
				ratio,
				3,
				msg=f"Expected ~O(log n), but going from n={n1} to n={n2} "
					f"took {ratio:.2f}x longer"
			)


if __name__ == '__main__':
	unittest.main()
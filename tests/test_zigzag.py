import unittest

from src.zigzag import ZigZag  

class TestZigZag(unittest.TestCase):
    def setUp(self):
        self.zigzag = ZigZag()

    def test_example_1(self):
        numbers = [1, 2, 1, 3, 4]
        expected = [1, 1, 0]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_example_2_all_increasing(self):
        numbers = [1, 2, 3, 4]
        expected = [0, 0]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_example_3_all_equal(self):
        numbers = [1000000000, 1000000000, 1000000000]
        expected = [0]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_min_length_3_zigzag_true(self):
        numbers = [1, 3, 2]
        expected = [1]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_min_length_3_zigzag_false(self):
        numbers = [1, 2, 3]
        expected = [0]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_mixed_pattern(self):
        numbers = [1, 3, 2, 1, 3, 2]
        # triples:
        # (1,3,2) -> zigzag (1 < 3 > 2)
        # (3,2,1) -> not zigzag (3 > 2 > 1)
        # (2,1,3) -> zigzag (2 > 1 < 3)
        # (1,3,2) -> zigzag (1 < 3 > 2)
        expected = [1, 0, 1, 1]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_no_zigzags_decreasing(self):
        numbers = [5, 4, 3, 2, 1]
        # (5,4,3), (4,3,2), (3,2,1) all strictly decreasing → no zigzag
        expected = [0, 0, 0]
        self.assertEqual(self.zigzag.solution(numbers), expected)

    def test_with_plateaus(self):
        numbers = [1, 2, 2, 1, 2]
        # (1,2,2) -> not zigzag (1 < 2 == 2)
        # (2,2,1) -> not zigzag (2 == 2 > 1)
        # (2,1,2) -> zigzag (2 > 1 < 2)
        expected = [0, 0, 1]
        self.assertEqual(self.zigzag.solution(numbers), expected)

if __name__ == "__main__":
    unittest.main()

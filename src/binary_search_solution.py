"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List

class BinarySearchSolution:

    def search(self, nums: List[int], target: int) -> int:
        low_pointer = 0
        high_pointer = len(nums)-1

        while low_pointer <= high_pointer:
                
            middle_index = (high_pointer + low_pointer) // 2
            middle_element = nums[middle_index]

            if middle_element == target:
                return middle_index
            elif middle_element < target:
                low_pointer = middle_index + 1
            elif middle_element > target:
                high_pointer = middle_index - 1

        return -1
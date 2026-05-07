"""
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time
complexity and with the smallest space complexity possible.
"""

from typing import List

class MergeSortSolution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    
    def merge_sort(self, array):
        length = len(array)

        if length < 2:
            return array

        # [:i] is a slicing notation used to extract a portion of a sequence (like a list, string, or array) up to, 
        # but not including, index i. first_half = arr[:i], second_half = arr[i:].
        middle = length // 2
        leftHalf = array[:middle]
        rightHalf = array[middle:]

        sortedLeftHalf = self.merge_sort(leftHalf)
        sortedRightHalf = self.merge_sort(rightHalf)

        return self.merge(sortedLeftHalf, sortedRightHalf)

    # Compare first element of each half, append lowest to mergedArray, remove this smallest element from original array,
    # do this again until one array is empty, then simply append the remaining array (which is already sorted) 
    # to the mergedArray, but use extend() so list elements are added, not list itself.
    def merge(self, leftHalf, rightHalf):

        mergedArray = []

        while leftHalf and rightHalf:

            if leftHalf[0] <= rightHalf[0]:
                mergedArray.append(leftHalf.pop(0))
            else:
                mergedArray.append(rightHalf.pop(0))

        if leftHalf:
            mergedArray.extend(leftHalf)
        else: 
            mergedArray.extend(rightHalf)

        return mergedArray   
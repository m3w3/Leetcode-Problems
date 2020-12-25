"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        valley_index = smallest_non_neg_index(nums, n)
        asc_min_index, desc_min_index = valley_index, valley_index - 1
        nums, sorted_nums = [num ** 2 for num in nums], []
        
        # essentially merging 2x sorted lists at this point
        while 0 <= desc_min_index and asc_min_index < n:
            if nums[asc_min_index] < nums[desc_min_index]:
                sorted_nums.append(nums[asc_min_index])
                asc_min_index += 1
            else:
                sorted_nums.append(nums[desc_min_index])
                desc_min_index -= 1
        # handle any remaining values not placed
        while 0 <= desc_min_index:
            sorted_nums.append(nums[desc_min_index])
            desc_min_index -= 1
        while asc_min_index < n:
            sorted_nums.append(nums[asc_min_index])
            asc_min_index += 1
        
        return sorted_nums
    
def smallest_non_neg_index(nums, n):
    if n == 1: return 0
    curr_index = 0
    while curr_index < n:
        if nums[curr_index] >= 0: return curr_index
        curr_index += 1
    return curr_index - 1

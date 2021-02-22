"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max, prev_max = float('-inf'), 0
        for i, num in enumerate(nums):
            # calculate max sum ending at current i
            if prev_max > 0: curr_max = prev_max + num
            else: curr_max = num
            # update local, global
            global_max = max(global_max, curr_max)
            prev_max = curr_max
        return global_max

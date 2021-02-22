"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # base case
        n = len(nums)
        if n == 0: return 0
        
        curr_sum, global_len_min = nums[0], float('inf')
        lo, hi = 0, 0 # indices of [lo,lo+1,...,hi]
        while hi < n:
            # search for right-most 'hi'
            if curr_sum < s:
                hi += 1
                if hi < n: curr_sum += nums[hi]
                continue
            # search for right-most 'lo'
            while lo < hi:
                if curr_sum - nums[lo] >= s:
                    curr_sum -= nums[lo]
                    lo += 1
                else: break
            global_len_min = min(global_len_min, hi - lo + 1)
            # continue to next possible section
            lo += 1
            hi += 1
            if hi < n: curr_sum = curr_sum - nums[lo - 1] + nums[hi]
        if global_len_min == float('inf'): return 0
        return global_len_min

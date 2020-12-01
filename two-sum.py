class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_examined = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in prev_examined:
                prev_examined[num] = i
            else:
                return [i, prev_examined[diff]]

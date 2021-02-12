class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]

        arr = [None for _ in nums]
        # base case:
        # length = 1 -> nums[0]
        # lenght = 2 -> max(nums[0], nums[1])
        arr[0], arr[1] = nums[0], max(nums[0], nums[1])

        # recursive case:
        # either take element nums[i], or don't
        # maximum of:
        # 1) take: nums[i] + rob(nums[0,...,i-2])
        # 2) don't take: rob(nums[0,...,i-1])
        for i in range(2, n):
            arr[i] = max(arr[i-1], arr[i-2] + nums[i])
        return arr[-1]
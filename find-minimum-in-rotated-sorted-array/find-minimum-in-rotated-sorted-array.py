class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while(1):
            size = hi - lo
            if size < 3: return min(nums)
            
            mid = lo + size // 2
            # min is on right side of mid
            if nums[mid] > nums[hi]:
                lo = mid
            # min is on left side of mid
            elif nums[lo] > nums[mid]:
                hi = mid
            else:
                return nums[lo]
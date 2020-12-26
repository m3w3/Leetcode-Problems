"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
"""

from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            if len(min_heap) < K:
                heappush(min_heap, (-(point[0]**2 + point[1]**2), point))
            else:
                curr_neg_dist = -(point[0]**2 + point[1]**2)
                # i.e. point = -19, curr_root = -20 -> put into heap
                if curr_neg_dist > min_heap[0][0]:
                    heapreplace(min_heap, (curr_neg_dist, point))
        return [heap_element[1] for heap_element in min_heap]

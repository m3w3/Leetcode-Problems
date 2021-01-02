"""
1640. Check Array Formation Through Concatenation
https://leetcode.com/problems/check-array-formation-through-concatenation/
"""
​
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = dict(zip([piece[0] for piece in pieces], pieces))
        i = 0
        while i < len(arr):
            if arr[i] not in d: return False
            piece = d[arr[i]]
            j = 0
            while j < len(piece) and i < len(arr):
                if piece[j] != arr[i]: return False
                i += 1
                j += 1
            if j != len(piece): return False
        return True

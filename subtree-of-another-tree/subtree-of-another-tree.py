"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None or t is None: return False
        return self.is_equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def is_equal(self, s, t) -> bool:
        # base case
        if s is None: return t is None
        elif t is None: return s is None
        
        # recursive case
        if s.val == t.val:
            return self.is_equal(s.left, t.left) and self.is_equal(s.right, t.right)
        return False

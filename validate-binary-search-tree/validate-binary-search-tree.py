"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""
​
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return helper(root)
        
def helper(node, lower=float('-inf'), upper=float('inf')):
    if not node: return True
    
    curr_val = node.val
    if upper <= curr_val or curr_val <= lower: return False
    
    if not helper(node.right, curr_val, upper): return False
    if not helper(node.left, lower, curr_val): return False
    
    return True

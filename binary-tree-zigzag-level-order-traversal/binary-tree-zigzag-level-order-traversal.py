# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        else: zigzag, q, left_to_right = [[root.val]], deque(), -1
            
        if root.right: q.append(root.right)
        if root.left: q.append(root.left)
            
        while q: # to visit each level
            temp, values = [], []
            while q: # to visit each node within the level
                node = q.popleft()
                values.append(node.val)
                if left_to_right == -1: # right_to_left
                    if node.right: temp.append(node.right)
                    if node.left: temp.append(node.left)
                else: # left_to_right
                    if node.left: temp.append(node.left)
                    if node.right: temp.append(node.right)
            left_to_right *= -1
            zigzag.append(values)
            q = deque(temp[::-1])
        
        return zigzag

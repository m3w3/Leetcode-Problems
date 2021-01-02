"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
"""
​
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Solve using simple BFS
        original_q = deque([original])
        cloned_q = deque([cloned])
        while original_q:
            curr_original, curr_cloned = original_q.popleft(), cloned_q.popleft()
            if target == curr_original: return curr_cloned
            if curr_original.left:
                original_q.append(curr_original.left)
                cloned_q.append(curr_cloned.left)
            if curr_original.right:
                original_q.append(curr_original.right)
                cloned_q.append(curr_cloned.right)

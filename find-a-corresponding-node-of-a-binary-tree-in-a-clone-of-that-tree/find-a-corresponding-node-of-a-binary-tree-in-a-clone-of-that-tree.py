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
        queue = deque([cloned])
        while queue:
            curr_node = queue.popleft()
            if target.val == curr_node.val: return curr_node
            if curr_node.left: queue.append(curr_node.left)
            if curr_node.right: queue.append(curr_node.right)

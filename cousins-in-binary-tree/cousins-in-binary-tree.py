# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, y_depth = find_depth(root, 0, x), find_depth(root, 0, y)
        same_depth = x_depth != -1 and x_depth == y_depth
        x_y_siblings = are_siblings(root, x, y)
        return True if same_depth and not x_y_siblings else False
    
def find_depth(root, curr_depth, value):
    if root is None: return -1
    if root.val == value: return curr_depth
    return max(find_depth(root.left, curr_depth + 1, value), find_depth(root.right, curr_depth + 1, value))
​
def are_siblings(root, x, y):
    if not root.left and not root.right: return False
    if not root.left: return are_siblings(root.right, x, y)
    if not root.right: return are_siblings(root.left, x, y)
    siblings = (root.left.val == x and root.right.val == y) or (root.left.val == y and root.right.val == x)
    if siblings: return True
    return are_siblings(root.right, x, y) or are_siblings(root.left, x, y)

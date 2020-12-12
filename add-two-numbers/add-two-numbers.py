"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode()
        p1, p2, p3 = l1, l2, new_head
        carry = 0
        
        while p1 and p2:
            added_val = p1.val + p2.val + carry
            carry, curr_val = added_val // 10, added_val % 10
            p3.next = ListNode(curr_val)
            p1, p2, p3 = p1.next, p2.next, p3.next
​
        while p1:
            added_val = p1.val + carry
            carry, curr_val = added_val // 10, added_val % 10
            p3.next = ListNode(curr_val)
            p1, p3 = p1.next, p3.next
        
        while p2:
            added_val = p2.val + carry
            carry, curr_val = added_val // 10, added_val % 10
            p3.next = ListNode(curr_val)
            p2, p3 = p2.next, p3.next
        
        if carry != 0:
            p3.next = ListNode(1)
        
        return new_head.next

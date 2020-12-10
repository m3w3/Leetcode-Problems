"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""
​
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val < l2.val: 
                curr.next = l1
                curr, l1 = curr.next, l1.next
            else: 
                curr.next = l2
                curr, l2 = curr.next, l2.next
                
        # hit end of one of the two (maybe both) linked lists
        # append rest of l1
        while l1:
            curr.next = l1
            curr, l1 = curr.next, l1.next
        # append rest of l2
        while l2:
            curr.next = l2
            curr, l2 = curr.next, l2.next
        
        return head.next

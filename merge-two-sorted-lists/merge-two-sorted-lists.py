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
        curr_l1, curr_l2 = l1, l2
        while curr_l1 and curr_l2:
            if curr_l1.val < curr_l2.val: 
                curr.next = ListNode(val=curr_l1.val)
                curr, curr_l1 = curr.next, curr_l1.next
            else: 
                curr.next = ListNode(val=curr_l2.val)
                curr, curr_l2 = curr.next, curr_l2.next
                
                
        # hit end of one of the two (maybe both) linked lists
        # append rest of l2
        while curr_l2:
            curr.next = ListNode(val=curr_l2.val)
            curr, curr_l2 = curr.next, curr_l2.next
        # append rest of l1
        while curr_l1:
            curr.next = ListNode(val=curr_l1.val)
            curr, curr_l1 = curr.next, curr_l1.next
        
        return head.next

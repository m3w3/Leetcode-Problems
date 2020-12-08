"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        curr = head
        curr_prev, curr_next = None, head.next
        while curr_next:
            curr.next = curr_prev
            curr_prev = curr
            curr = curr_next
            curr_next = curr.next
        curr.next = curr_prev
        head = curr
        return head

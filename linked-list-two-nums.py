"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.read_list(l1)
        n2 = self.read_list(l2)
        return self.write_list(n1 + n2)
    
    def read_list(self, root):
        num = 0
        multiple = 1
        while root:
            num += multiple * root.val
            multiple *= 10
            root = root.next
        return num
    
    def write_list(self, num):
        if not num:
            return ListNode()
        root = head = ListNode()
        while num:
            head.next = ListNode(num % 10)
            num //= 10
            head = head.next
        return root.next  
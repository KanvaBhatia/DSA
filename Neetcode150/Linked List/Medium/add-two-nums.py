# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        tmp1, tmp2, tmp3 = l1, l2, final
        carry = 0
        while tmp1 and tmp2:
            val = tmp1.val + tmp2.val + carry
            carry = 1 if val >= 10 else 0
            tmp = ListNode(val % 10)
            final.next = tmp
            final = final.next
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        while tmp1:
            val = tmp1.val + carry
            carry = 1 if val >= 10 else 0
            tmp = ListNode(val % 10)
            final.next = tmp
            final = final.next
            tmp1 = tmp1.next
        while tmp2:
            val = tmp2.val + carry
            carry = 1 if val >= 10 else 0
            tmp = ListNode(val % 10)
            final.next = tmp
            final = final.next
            tmp2 = tmp2.next
        if carry:
            tmp = ListNode(1)
            final.next = tmp
        return tmp3.next
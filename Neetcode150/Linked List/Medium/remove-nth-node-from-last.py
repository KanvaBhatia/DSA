# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        to_pass = count - n
        tmp = head
        prev = None
        while to_pass:
            prev = tmp
            tmp = tmp.next
            to_pass -= 1
        if prev:
            prev.next = tmp.next
            return head
        else:
            head = head.next
            return head
        
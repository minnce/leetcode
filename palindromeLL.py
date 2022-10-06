# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        pal = ""
        pal2 = ""
        while head:
            pal += str(head.val)
            pal2 += str(head.val)
            head = head.next
        pal = list(pal)
        pal2 = list(pal2)
        pal.reverse()
        return pal == pal2

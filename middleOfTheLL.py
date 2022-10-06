# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        dummy = ListNode()
        tail = dummy
        count2 = 0
        counter = 0
        countHead = head
        while countHead:
            counter+=1
            countHead=countHead.next
        counter = ((int(math.floor(float(counter)/2))))
        while head:
            if count2 >= counter:
                tail.next = head
                tail = tail.next
            count2+=1
            head = head.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fir = sec = head
        while fir != None and fir.next != None :
            fir = fir.next.next
            sec = sec.next
        return sec
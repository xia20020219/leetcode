# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listhead = ListNode()
        listhead.next = head
        fir, sec = listhead, listhead

        while n != 0 :
            fir = fir.next
            n -= 1
        
        while fir.next != None :
            sec = sec.next
            fir = fir.next
        
        sec.next = sec.next.next
        return listhead.next
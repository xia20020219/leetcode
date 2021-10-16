# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         if isinstance(val, int):
#             self.val = val
#             self.next = next
            
#         elif isinstance(val,list):
#             self.val = val[0]
#             self.next = None
#             cur = self
#             for i in val[1:]:
#                 cur.next = ListNode(i)
#                 cur = cur.next

#     def gatherAttrs(self):
#         return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

#     def __str__(self):
#             return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #if isinstance(l1,list):
        #    l1 = ListNode(l1)
        #    l2 = ListNode(l2)
        head = ListNode(l1.val + l2.val)
        num = head
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            num.next = ListNode(l1.val + l2.val + num.val//10)
            num.val = num.val % 10
            num = num.next
        if num.val >= 10:
            num.next = ListNode(num.val // 10)
            num.val = num.val % 10
        return head
    
#if __name__ == "__main__":
#    test = Solution()
#    print(test.addTwoNumbers([1,3],[2,1,3]))
# 取自https://leetcode-cn.com/problems/add-two-numbers/solution/python3ti-jie-fang-leetcodeguan-fang-lei-listnoded/

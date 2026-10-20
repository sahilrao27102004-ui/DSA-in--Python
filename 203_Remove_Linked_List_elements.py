# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        t=headA
        t1=headB
        arr=set()
        while t !=None:
            arr.add(t)
            t=t.next

        while t1!=None:
            if t1 in arr:
                return t1
            t1=t1.next
        return None
    
        

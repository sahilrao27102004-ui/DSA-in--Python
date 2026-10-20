# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        t=head
        count=0
        while t!=None:
            t=t.next
            count+=1
        t=head
        decimal=0
        for i in range(count):
            decimal=decimal+t.val*2**(count-i-1)
            t=t.next
            
        return decimal
        
            
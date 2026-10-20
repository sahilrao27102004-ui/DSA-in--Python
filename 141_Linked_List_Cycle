# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t=head
        arr=[]
        while t!=None:
            if t in arr:
                return True
            arr.append(t)
            t=t.next
        
        return False
        


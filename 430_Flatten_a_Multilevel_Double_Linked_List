"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        t=head
        Next=None
        while t!=None:

            if t.child!=None:
                Next=t.next
                t.next=self.flatten(t.child)
                t.next.prev=t
                t.child=None

                while t.next!=None:
                    t=t.next
                t.next=Next
                if Next!=None:
                    Next.prev=t 
            else:
                t=t.next

        return head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        '''
        pre = None
        cur = head
        h = head
        while cur:
            h = cur
            tmp = cur.next
            cur.next = pre
            pre=cur
            cur=tmp
        return h

'''
        
sol = Solution()
head =ListNode(1)
p1=ListNode(2)
p2=ListNode(3)
p3=ListNode(4)
head.next=p1
p1.next=p2
p2.next=p3

p = sol.reverseList(head)
while p:
    print p.val
    p=p.next





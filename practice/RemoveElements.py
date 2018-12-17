# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []

        link_head = ListNode(None)
        link_head.next = head
        head = link_head

        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next

            else:
                head = head.next
        return link_head.next


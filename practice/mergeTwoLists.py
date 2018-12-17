# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        #list type
        newlist = []
        while len(l1)>0 and len(l2)>0:
            if l1[0] < l2[0]:
                newlist.append(l1[0])
                del l1[0]
            else:
                newlist.append(l2[0])
                del l2[0]
        newlist.extend(l1)
        newlist.extend(l2)
        print newlist

        '''
        # listNode type
        newlist = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        print newlist.next

sol = Solution()
ln1 = ListNode(3)
ln2 = ListNode(4)
sol.mergeTwoLists(ln1, ln2)
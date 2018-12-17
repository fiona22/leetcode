# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):

        if listNode.val == None:
            return []
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

test = ListNode()
S = Solution()

print S.printListFromTailToHead(node1)
# coding=utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 开辟新空间的方法
def func1(head):
    if head==None or head.next==None:
        return head
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    newhead = ListNode(0)
    tmp = newhead
    for i in arr[::-1]:
        tmp.next = ListNode(i)  # 元素插入新的链表
        tmp = tmp.next
    return newhead.next

'''
开始以单链表的第一个元素为循环变量cur,并设置2个辅助变量tmp,保存数据;
newhead,新的翻转链表的表头。
时间消耗O(n),空间消耗O(1)
'''
def func2(head):
    if head==None or head.next==None:
        return head
    cur = head  # 循环变量
    tmp = None  # 保存数据的临时变量
    newhead = None  # 新的翻转单链表的表头
    while cur:
        tmp = cur.next
        cur.next = newhead
        newhead = cur
        cur = tmp
    return newhead



# 递归方法
def func3(head):
    if head.next == None:
        return head
    new_head = func3(head.next)
    head.next.next = head
    head.next = None
    return new_head


def create_ll(arr):
    pre = ListNode(0)
    tmp = pre
    for i in arr:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return pre.next

def print_ll(head):
    tmp = head
    while tmp:
        print tmp.val
        tmp=tmp.next


a = create_ll(range(5))
print_ll(a)  # 0 1 2 3 4
a = func1(a)
print_ll(a)  # 4 3 2 1 0

a = func2(a)
print_ll(a)  # 0 1 2 3 4
a = func3(a)
print_ll(a)  # 4 3 2 1 0

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = pre = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = ListNode(l1.val)
                l1 = l1.next
            else:
                pre.next = ListNode(l2.val)
                l2 = l2.next
            pre = pre.next
        while l1:
            pre.next = ListNode(l1.val)
            l1 = l1.next
            pre = pre.next
        while l2:
            pre.next = ListNode(l2.val)
            l2 = l2.next
            pre = pre.next

        return res.next


if __name__ == '__main__':
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(1)
    l1.next = l11 = ListNode(2)
    l11.next = l12 = ListNode(4)
    # 定义l2链表
    l2 = ListNode(1)
    l2.next = l21 = ListNode(3)
    l21.next = l22 = ListNode(4)
    # 获取返回值的链表
    res = sol.mergeTwoLists(l1, l2)
    # 循环遍历出来
    while res:
        print(res.val)
        res = res.next

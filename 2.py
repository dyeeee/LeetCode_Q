
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 这里一开始不做l1、l2非空判断，题意表明非空链表
        # 记录是否需要增加新节点，或在链表下一个节点是否需要加1，同时记录链表同级节点的和
        carry = 0
        # 这里的执行顺序是res = ListNode(0), pre = res
        res = pre = ListNode(0)
        # 判断l1、l2、carry是否有值，carry有值的话需要增加新节点，或在链表下一个节点需要加1
        while l1 or l2 or carry:
            # 判断l1是否有值
            if l1:
                carry += l1.val
                l1 = l1.next
            # 判断l2是否有值
            if l2:
                carry += l2.val
                l2 = l2.next
            # carry有同级节点的和(同个位/十位..)
            # divmod返回商与余数的元组，拆包为carry和val
            # carry有值的话需要增加新节点，或在链表下一个节点需要加1,在循环中会用到
            carry, val = divmod(carry, 10)  # 解决进位问题
            # 新建链表节点
            pre.next = pre  = ListNode(val)
        # 返回res.next
        return res.next


if __name__ == '__main__':
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(3)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    # 获取返回值的链表
    res = sol.addTwoNumbers(l1, l2)
    # 循环遍历出来
    while res:
        print(res.val)
        res = res.next
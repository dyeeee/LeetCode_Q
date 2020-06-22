# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 输入:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# 输出: ["1->2->5", "1->3"]
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        tmp = root
        reslist = []
        res = str(root.val)

        


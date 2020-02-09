# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    # 超时
    def generateParenthesis_1(self, n: int):
        result = []
        s_list = []
        from itertools import permutations
        for i in permutations('()' * n):
            s_list.append("".join(i))
        s_list = list(set(s_list))

        def isValid(str):
            symDic = {'(': 1, ')': -1}
            count = 0
            for s in str:
                count += symDic[s]
                if count < 0:
                    return False

            return True

        for s in s_list:
            if isValid(s):
                result.append(s)
        result = list(set(result))
        result.sort()
        return result

    # 只有在我们知道序列仍然保持有效时才添加'(' or ')'，而不是像方法一
    # 那样每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
    # 如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。

    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:  # 直到某串长度符合
                ans.append(S)
                return
            if left < N:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans

    # 思路
    #
    # 为了枚举某些内容，我们通常希望将其表示为更容易计算的不相交子集的总和。
    #
    # 考虑有效括号序列S的闭包数：至少存在index >= 0，使得
    # S[0], S[1], ..., S[2 * index + 1]
    # 是有效的。 显然，每个括号序列都有一个唯一的闭包号。 我们可以尝试单独列举它们。
    #
    # 算法
    # 对于每个闭合数c，我们知道起始和结束括号必定位于索引0和2 * c + 1。
    # 然后两者间的2 * c个元素一定是有效序列，其余元素一定是有效序列。

    def generateParenthesis_advanced(self, N):
        if N == 0:
            return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = 5
    r1 = sol.generateParenthesis(s)
    print(r1)

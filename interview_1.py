# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 返回可以通过分割得到的平衡字符串的最大数量。

# 示例 1：
# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。

# 示例 2：
# 输入：s = "RLLLLRRRLR"
# 输出：3
# 解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。

# 示例 3：
# 输入：s = "LLLLRRRR"
# 输出：1
# 解释：s 只能保持原样 "LLLLRRRR".

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        slist = list(s)
        count_1 = 1
        count_2 = 0
        current = slist[0]
        for i in range(1, len(slist)):
            #print(i)
            if slist[i] != current:
                count_2 += 1
                if count_2 == count_1:
                    res += 1
                    if i == len(slist) - 1:
                        break
                    else:
                        current = slist[i+1]
            else:
                count_1 += 1



        return res



if __name__ == '__main__':
    sol = Solution()
    h = 'RLRRLLRLRL'
    r1 = sol.balancedStringSplit(h)
    print(r1)

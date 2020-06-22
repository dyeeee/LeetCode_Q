# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        '''
        :type strs: List(strs)
        :rtype: str
        '''
        result = ""
        min_len = 2 ** 32
        result_list = []
        j = 0
        if len(strs) == 0 :
            return ""

        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        tag = True
        for i in range(min_len):
            while j < len(strs) - 1:
                if strs[j + 1][i] != strs[j][i]:
                    # print(strs[j + 1][i], strs[j][i])
                    tag = False
                    result = "".join(result_list)
                    return result
                j += 1
            if tag:
                result_list.append(strs[j][i])
            j = 0
            # print(result_list)

        result = "".join(result_list)

        return result


if __name__ == '__main__':
    sol = Solution()
    t = ["abc"]
    r1 = sol.longestCommonPrefix(t)
    print(r1)

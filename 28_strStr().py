# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


if __name__ == '__main__':
    sol = Solution()
    h = 'hello'
    n = 'll'
    r1 = sol.strStr(h, n)
    print(r1)

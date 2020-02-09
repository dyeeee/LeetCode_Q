class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size == 0:
            return ''

        # 至少是 1
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub

        return longest_palindrome_str

    # 中心扩散
    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        l = left
        r = right

        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1



if __name__ == '__main__':
    sol = Solution()
    h = 'hello'
    r1 = sol.longestPalindrome(h)
    print(r1)


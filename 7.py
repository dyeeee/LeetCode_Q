# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
# 输入: 123
# 输出: 321
#
#  示例 2:
# 输入: -123
# 输出: -321
#
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution:
    def reverse(self, x: int) -> int:
        result_list = []
        if x < 0:
            result_list.append('-')
            x = abs(x)

        x_list = list(str(x))
        x_list.reverse()

        num = ''.join(x_list)
        result_list.append(num)
        result = int(''.join(result_list))
        if result < -2**31 or result > 2**30:
            result = 0

        return result


if __name__ == '__main__':
    sol = Solution()
    t = 123
    r1 = sol.reverse(t)
    print(r1)

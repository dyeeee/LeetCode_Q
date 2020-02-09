# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
#
# 注意：整数顺序将表示为一个字符串。


class Solution2:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person

class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(1, n):
            tmp, content, count = '', result[0], 1  # 初始化
            for j in range(1, len(result)):
                # 和当前content相等则计数器+1
                if result[j] == content:
                    count += 1
                # 否则结算并重置content
                else:
                    tmp += str(count) + content
                    content = result[j]
                    count = 1
            tmp += str(count) + content
            result = tmp

        return result


if __name__ == '__main__':
    sol = Solution()
    s = 4
    a = sol.countAndSay(s)
    print(a)


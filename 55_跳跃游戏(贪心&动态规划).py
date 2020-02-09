#
# 贪心/动态规划的题目
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

# 示例 2:
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


# 贪心：尽可能到达最远的地方，只要能到达某个位置，一定能到达他之前的所有位置（跳数为最大长度，可以只跳一步）

class Solution:
    # 这个解法有错误，没有考虑到不跳最远反而可以到达的情况
    def canJump_WRONG(self, nums: list) -> bool:
        result = False
        index = 0
        for i, step in enumerate(nums):
            if i != index:
                continue
            index += step
        if index >= len(nums) - 1:
            result = True

        return result

    def canJump(self, nums: list) -> bool:
        result = False
        index = 0  # 最大可达索引
        for i, step in enumerate(nums):
            # 如果当前位置小于等于最大索引，意味着当前位置可达
            # 当前位置索引加上step大于最大索引的话则更新最大可达索引
            if index >= i and i + step >= index:
                index = i + step

        if index >= len(nums) - 1:
            result = True

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 5, 0, 0]
    r1 = sol.canJump(nums)
    print(r1)

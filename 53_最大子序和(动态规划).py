# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution:
    def removeDuplicates(self, nums) -> int:
        dynamicProgram = []
        dynamicProgram.append(nums[0])
        result = nums[0]

        for i in range(1, len(nums)):
            dynamicProgram.append(max(dynamicProgram[i - 1] + nums[i], nums[i]))
            if result < dynamicProgram[i]:
                result = dynamicProgram[i]

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    r1 = sol.removeDuplicates(nums)
    print(r1)

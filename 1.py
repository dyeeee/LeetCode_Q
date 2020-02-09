class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 用len()方法取得nums列表长度
        n = len(nums)
        # 创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]], x
            # 否则往字典增加键/值对
            else:
                d[a] = x  # 数字a加nums[x]=target,在之后若出现数字a，则证明其存在nums中，位置为当前x。数字a作为键对应的值是能和a组成target的位置x。
        return []



if __name__ == '__main__':
    nums = [2, 7, 9, 10, 11, 12]
    solution = Solution()
    result = solution.twoSum(nums=nums, target=11)

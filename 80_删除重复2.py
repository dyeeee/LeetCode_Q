class Solution:
    def removeDuplicates(self, nums) -> int:
        countDic = {}
        for i in set(nums):
            countDic[i] = nums.count(i)

        for num in nums:
            while countDic[num] > 2:
                nums.pop(nums.index(num))
                countDic[num] -= 1


        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,2,2,3]
    r1 = sol.removeDuplicates(nums)
    print(r1)
    print(nums[0:r1])

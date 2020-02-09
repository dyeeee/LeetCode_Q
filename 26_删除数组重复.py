class Solution:
    def removeDuplicates(self, nums) -> int:
        a = list(set(nums))
        a.sort()
        nums.clear()
        for i in range(len(a)):
            nums.append(a[i])

        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2]
    r1 = sol.removeDuplicates(nums)
    print(r1)
    print(nums[0:r1])

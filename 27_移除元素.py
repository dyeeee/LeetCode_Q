class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        while 1:
            if val in nums:
                nums.pop(nums.index(val))
            else:
                return len(nums)


if __name__ == '__main__':
    sol = Solution()
    s1 = [1, 2, 3]
    r1 = sol.removeElement(s1,1)
    print(r1)

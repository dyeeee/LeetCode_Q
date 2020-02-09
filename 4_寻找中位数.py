class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 0:
            m1 = int(length / 2 - 1)
            m2 = int(length / 2)
            median_num = (nums[m1] + nums[m2]) / 2
        else:
            m = int(length/2-0.5)
            median_num = nums[m]

        return median_num


if __name__ == '__main__':
    sol = Solution()
    h = [1, 3]
    n = [2]
    r1 = sol.findMedianSortedArrays(h, n)
    print(r1)

# 给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
# 如果不存在这样的下标 index，就请返回 -1。
# 何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
# 首先，A.length >= 3
# 其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
#
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# 你将不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
# MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
# MountainArray.length() - 会返回该数组的长度


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.size


class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        size = mountain_arr.length()

        # 步骤 1：先找到山顶元素所在的索引
        mountaintop = self.__find_mountaintop(mountain_arr, 0, size - 1)

        # 步骤 2：在前有序且升序数组中找 target 所在的索引
        res = self.__find_from_sorted_arr(mountain_arr, 0, mountaintop, target)
        if res != -1:
            return res

        # 步骤 3：如果步骤 2 找不到，就在后有序且降序数组中找 target 所在的索引
        return self.__find_from_inversed_arr(mountain_arr, mountaintop + 1, size - 1, target)

    def __find_mountaintop(self, mountain_arr: 'MountainArray', l: int, r: int):
        # 返回山顶元素
        while l < r:
            mid = l + (r - l) // 2
            # 取左中位数，因为进入循环，数组一定至少有 2 个元素
            # 因此，左中位数一定有右边元素，数组下标不会发生越界
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # 如果当前的数比右边的数小，它一定不是山顶
                l = mid + 1
            else:
                r = mid
        # 根据题意，山顶元素一定存在，因此退出 while 循环的时候，不用再单独作判断
        return l

    def __find_from_sorted_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在前有序且升序数组中找 target 所在的索引
        while l < r:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        # 因为不确定区间收缩成 1 个数以后，这个数是不是要找的数，因此单独做一次判断
        if mountain_arr.get(l) == target:
            return l
        return -1

    def __find_from_inversed_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在后有序且降序数组中找 target 所在的索引
        while l < r:
            mid = l + (r - l) // 2
            # 与 __find_from_sorted_arr 方法不同的地方仅仅在于由原来的小于号改成大于号
            if mountain_arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        return -1


    def binary_search(self, nums, target):
        size = len(nums)
        left = 0
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2  # 区间内的左中位数  # mid = int((low + high) / 2)
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间是 [left, mid]
                right = mid

    def binary_searc_2(mountain, target, l, r, key=lambda x: x):
        target = key(target)
        while l <= r:
            mid = (l + r) // 2
            cur = key(mountain.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1



if __name__ == '__main__':
    arr = [1,2,3,4,5,3,1]
    mountain_array = MountainArray(arr)
    target = 3
    solution = Solution()
    res = solution.findInMountainArray(target, mountain_array)
    print('res', res)

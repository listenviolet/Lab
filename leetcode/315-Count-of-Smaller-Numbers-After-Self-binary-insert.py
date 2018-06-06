class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        # nums = nums[::-1]
        n = len(nums)
        ans = [0] * n
        new_nums = []
        
        for i in range(n - 1, -1, -1):
            left, right = 0, len(new_nums)
            while(left < right):
                mid = left + (right - left) // 2
                if new_nums[mid] >= nums[i]: right = mid
                else: left = mid + 1
            ans[i] = right
            new_nums.insert(right, nums[i])
        return ans

# Solution:
# 和自己的想法一样，
# 但省去了先排序再检索在排序中序号的步骤
# 直接以逆序的方式，插入新的有序数组，找到在新有序数组中的ind
# 即为该元素在原数组中，右侧小于它的元素个数之和

# Beats: 90.32%
# Runtime: 152ms
# hard
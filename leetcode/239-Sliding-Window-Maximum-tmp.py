class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Max = []
        if not nums: return Max
        if k >= len(nums): 
            Max.append(max(nums))
            return Max
        
        tmp = max(nums[0: k])
        Max.append(tmp)
        for i in range(len(nums) - k):
            if nums[i] == tmp: 
                tmp = max(nums[i + 1: i + k + 1])
            else:
                tmp = max(tmp, nums[i + k])
            Max.append(tmp)
        return Max

# Solution:
# 上一个方法中每次移动，在k大小的窗口中求最大值
# 这是有重复的
# o****
#  ****o
# 所以本方法改进了
# 当上一个窗口o为上一个的最大值时，才需比较****o
# 否则，上一个窗口的最大值在****中，
# 新窗口最大值即为 max(tmp, 新进入窗口的nums[i + k])

# Beats: 49.55%
# Runtime: 229ms

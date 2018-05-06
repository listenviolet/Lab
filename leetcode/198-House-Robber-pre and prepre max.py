class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        money = [0,nums[0]]
        for i in range(1,len(nums)):
            temp = money[0]
            money[0] = max(money[0],money[1])
            money[1] = temp + nums[i]
        return max(money[0],money[1])

# Solution: *******+O
# money[0] 记录当前前两个及之前的最大值 --> * 的最大值
# money[1] 记录当前的前一个的最大值 --> +的值
# 当前最大为money[0] + nums[i] -->用temp代替，更替money[0]为原money[1]
# nums序列中最大为max(money[0], money[1])

# 和自己的方法相比：
# 无需维护大小为n的dp数组，仅保存有价值的前一个最大值和前两个最大值

# Beats: 98.56%
# Runtime: 36ms
# easy
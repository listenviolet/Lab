class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        l = list(set(nums))
        l.sort()
        Max = 1
        temp = 1
        for i in range(len(l) - 1):
            if l[i + 1] == l[i] + 1:
                temp = temp + 1
                if temp > Max:
                    Max = temp
                continue
            else:                
                temp = 1
        return Max

# Question:
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Solution:
# Note: 首先借助set去除nums中的重复元素
# 将l排序
# 依次判断两元素是否连续，若连续temp + 1
# 若temp长度大于最大连续长度，则更新Max
# Note: Max与temp均从1开始
# Beats: 93.73%
# Hard
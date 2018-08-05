class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_num = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp_num:
                return (tmp_num[target - nums[i]], i)
            else:
                tmp_num[nums[i]] = i;
        return (-1, -1)

# Description:
# Given an array of integers, 
# return indices of the two numbers such that 
# they add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Solution:
# 每遍历一个nums[i],判断target - nums[i]是否在nums中。
# 这里用到dict来存储nums中每一个值及其对应index。
# Notice:
# 应该先判断target - nums[i]是否在tmp_num中，
# 再将nums[i]添加到tmp_num中，
# 否则若先将nums[i]添加到tmp_num， 
# 则判断target - nums[i]时会将刚添加的nums[i]本身也算上。
# 错例：
# input:    [3, 2, 4] 6
# output:   [0, 0]  
# expected: [1, 2]
# 这里就是将刚添加的元素3算入了，应该先判断6 - 3是否在，再添加nums[0]

# Beats: 46.65%
# Runtime: 56ms
# easy
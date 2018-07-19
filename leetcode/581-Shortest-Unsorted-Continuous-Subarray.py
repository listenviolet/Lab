class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0] + nums[:]
        print(nums)
        start = 1
        end = 1
        
        i = 2
        while i < len(nums):
            if end == 1 and nums[i] >= nums[i - 1]:
                start += 1
            if nums[i] < nums[i - 1]:
                end = i
                
                if nums[i] >= nums[start]:
                    k = i - 1
                    while nums[k] > nums[i]:
                        k -= 1
                    nums[k + 1 : i + 1] = [nums[i]] + nums[k + 1: i]
                    continue
                if nums[i] < nums[start]:
                    while nums[start] > nums[i]:
                        start -= 1
                    nums[start + 1 : end + 1] = [nums[end]] + nums[start + 1 : end]
            i += 1
        return end - start if end > 1 else 0

# Description:
# Given an integer array, you need to find one continuous subarray 
# that if you only sort this subarray in ascending order, 
# then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order 
# to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, 
# so ascending order here means <=.

# # Solution: 
#                                                                     nums[i] < nums[i - 1]
#                                                                             |
# 0, 1, ... , start, [start + 1, start + 2, ... , end], end + 1, ... , i - 1, i, ..., n - 1
#        |                                                                    |
#     new start                                                            end   = i
#                                                                          start = start     -- nums[i] >= nums[start]
#                                                                                  new start -- nums[i] < nums[start]
# 以上实质判断nums[i]落在哪个区间里
# 若在[1, ... start]区间中，则要更新start, end = i
# 若在[start + 1, ..., end]区间中，则无需更新start,只更新end = i
# 
# Note:
# 起初在nums头部添加0元素
# start = 1, end = 1
# 以end == 1判断start是否被移动过
# 若end == 1 start从未被移动，那么，每次i+1, start + 1
# 若end > 1  start已被移动过，start的值即为当前subarray的开始标记，
#            则若未达到要调换start的条件(见上)则不可更改start值

# Time Limit Exceeded
# 209 / 307 test cases passed.

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        ans = []
        tmp = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    tmp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    # print("i:",i, "j:", j, "left:", left, "right:", right)
                    if tmp_sum == target: 
                        tmp = [nums[i], nums[j], nums[left], nums[right]]
                        if tmp not in ans:
                            ans.append(tmp)
                        left += 1
                        right -= 1
                    elif tmp_sum < target:
                        left += 1
                    else: right -= 1
        return ans

# Description:
# Given an array nums of n integers and an integer target, 
# are there elements a, b, c, and d in nums 
# such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# Solution:
# 同3sum
# 先固定i, j 前两个数，再按照left ->  <- right找后两个数
# 这里注意：
# 1. 当i,j固定时，后面可能有多组成立的情况
#    -3 -2 -1 0 0 1 2 3
#        *  *     | |
#               |      |
#     故不可以直接break, 而应该left += 1; right -= 1继续判断
# 2. 有可能遇到重复的情况
#    -3 -2 -1 0 0 1 2 3
#    *        |   * *
#    *          | * *  
#    这两个0为取不同的j时取到，但其值相同，为避免加入重复数组,
#    用 if tmp not in ans: ans.append(tmp) 先判断再添加.     
              
# Beats: 14.47%
# Runtime: 1440ms
# medium
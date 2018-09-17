class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # print(nums)
        nums.sort()
        # print(nums)
        mindiff = 100000
        res = 0
        
        for i in range(len(nums) - 2):
            # print("i: ", i)
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                # print("left:", left, "right", right)
                tmp_sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - tmp_sum)
                if diff < mindiff:
                    mindiff = diff
                    res = tmp_sum
                    
                if tmp_sum == target: return tmp_sum
                elif tmp_sum < target: left = left + 1
                else: right = right - 1
        return res

# Description:
# Given an array nums of n integers and an integer target, 
# find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Solution:
# ---*  O O O ............. O O
#    |  |                     |
#    i left->             <-right
                
# Beats: 83.83%
# Runtime: 104ms
# medium
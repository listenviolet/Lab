class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums = [1] + nums[:] + [1]
        print(nums)
        
        
        while True:
            n = len(nums)
            if n == 2: return ans
            
            elif n == 3: 
                ans += nums[1]
                ind = 1
            elif n == 4:
                Min = min(nums[1], nums[2])
                ind = nums[1 : n - 1].index(Min) + 1
                ans += nums[ind - 1] * nums[ind] * nums[ind + 1]
                
            elif n == 5:
                Min = min(nums[1: n - 1])
                if Min > 0:
                    ind = 2
                    ans += nums[ind - 1] * nums[ind] * nums[ind + 1]
                elif Min == 0:
                    ind = nums[1: n - 1].index(Min) + 1
            elif n > 5:
                Min = min(nums[1 : n - 1])
                ind = nums[1 : n - 1].index(Min) + 1
                ans += nums[ind - 1] * nums[ind] * nums[ind + 1]
            print(ind,ans)
            nums = nums[: ind] + nums[ind + 1:]

# Description
# Given n balloons, indexed from 0 to n-1. 
# Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. 
# If the you burst balloon i 
# you will get nums[left] * nums[i] * nums[right] coins. 
# Here left and right are adjacent indices of i. 
# After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect 
# by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. 
# They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:

# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

# Solution:
# 首先将数组扩充，比如
#   3 1 5 8
# 1 3 1 5 8 1

# 每次选取除两边的1以外的中间的最小值，
# 因为先去最小值，较大值会保留更长时间，
# 乘积之和更大
# 特殊情况是中间只有3个数
# 如果这三个数中有零，则先去除0
# 如果没有，则最小值>=1
# 那么三个数的乘积>=取任意一边的边界1的乘积
# --不一定 ->这里出现错误 如 
#                   1 10 1
#                 1 1 10 1 1
#                                                         
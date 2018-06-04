class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums: return []
        n = len(nums)
        count = [0] * n
        
        sorted_nums = nums[:]
        sorted_nums.sort()
        
        
        for i in range(n):
            ind = sorted_nums.index(nums[i])
            count[i] = ind
            sorted_nums = sorted_nums[:ind] + sorted_nums[ind + 1:]
        return count

# Description:
# You are given an integer array nums 
# and you have to return a new counts array. 
# The counts array has the property 
# where counts[i] is the number of smaller elements 
# to the right of nums[i].

# Example:

# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

# Solution:
# 先对nums排序
# 例如
# 0 1 2 3 4 5
# 5 1 8 3 2 7  -> nums
# 1 2 3 5 7 8  -> sorted_nums

# 遍历nums:
# 对于nums中每一个元素i，
# count[i]为小于它，且未在其左侧出现过的，
# 那么可以用一个sorted_nums数组，
# 从大到小对nums排序，
# 每遇到一个数nums[i],
# 该数在sorted_nums中的序号即为小于该数的元素总数
# 遍历该数后，将该数从sorted_nums中移除，
# 这样，再在sorted_nums中找其他数时，不会再算该数
# 因为该数在其他数的左侧，已被计算过

# 对于5：在sorted_nums中ind = 3,
# 即有三个元素比它小
# count[0] = ind = 3
# 然后因为5已经比较过，nums中5之后的元素不会再与5比较，
# 从sorted_nums中去除
# 0 1 2 3 4 5
# 5 1 8 3 2 7  -> nums
# 1 2 3 7 8  -> sorted_nums

# Time Limit Exceeded
# 15 / 16 test cases passed.
# hard
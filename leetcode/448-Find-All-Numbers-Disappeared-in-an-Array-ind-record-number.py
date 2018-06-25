class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        flags=[0]*(len(nums)+1)
        res=[]
        for num in nums:
            flags[num]=1
        for i in range(1,len(nums)+1):
            if flags[i]==0:
                res.append(i)
        return res

# Description:
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive 
# that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

# Solution:
# flags 的每一位的ind记录的是number
# nums中出现的数字num,在对应flags[num]位标记为1，
# 遍历flags数组，值为0的那些位ind，即为nums中空缺的值

# Beats: 99.59%
# Runtime: 148ms
# easy
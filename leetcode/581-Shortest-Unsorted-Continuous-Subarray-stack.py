class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        l = len(nums)
        r = 0

        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        
        stack = []
        
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        
        return r - l + 1 if r - l > 0 else 0

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

# Solution:
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
# Approach #4 Using Stack [Accepted]:

# Algorithm

# The idea behind this approach is also based on selective sorting. 
# We need to determine the correct position of the minimum 
# and the maximum element in the unsorted subarray 
# to determine the boundaries of the required unsorted subarray.

# To do so, in this implementation, we make use of a stackstack. 
# We traverse over the numsnums array starting from the beginning. 
# As we go on facing elements in ascending order(a rising slope), 
# we keep on pushing the elements' indices over the stackstack. 
# This is done because such elements are in the correct sorted order
# (as it seems till now). 
# As soon as we encounter a falling slope, i.e. an element nums[j] 
# which is smaller than the element on the top of the stackstack, 
# we know that nums[j]nums[j] isn't at its correct position.

# In order to determine the correct position of nums[j], 
# we keep on popping the elemnents from the top of the stack 
# until we reach the stage where the element(corresponding to the index)
# on the top of the stackstack is lesser than nums[j]. 
# Let's say the popping stops when the index on stack's top is k. 
# Now, nums[j] has found its correct position. 
# It needs to lie at an index k + 1.

# We follow the same process while traversing over the whole array, 
# and determine the value of minimum such kk. 
# This marks the left boundary of the unsorted subarray.

# Similarly, to find the right boundary of the unsorted subarray, 
# we traverse over the numsnums array backwards. 
# This time we keep on pushing the elements if we see a falling slope. 
# As soon as we find a rising slope, 
# we trace forwards now and determine the larger element's correct position. 
# We do so for the complete array and thus, 
# determine the right boundary.

# We can look at the figure below for reference. 
# We can observe that the slopes directly indicate the relative ordering. 
# We can also observe that the point bb needs to lie just after index 0 
# marking the left boundary and the point aa needs to lie just 
# before index 7 marking the right boundary of the unsorted subarray.

# Complexity Analysis

# Time complexity : O(n). Stack of size nn is filled.

# Space complexity : O(n). Stack size grows upto nn.

# Note:
# stack中存的是index, 而不是nums值。

# Beats: 4.05%
# Runtime: 188ms
# easy
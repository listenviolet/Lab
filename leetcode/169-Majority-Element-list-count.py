class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums_set = set(nums)
        
        for i in nums_set:
            num = nums.count(i)
            if num > n // 2:
                return i

# Solution:
# Use list.count(obj)

# Beats: 98.76%
# Runtime: 48ms
# easy
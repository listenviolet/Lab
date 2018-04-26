class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

# 2 * (a+b+c)−(a+a+b+b+c)=c
# Beats: 95.12%
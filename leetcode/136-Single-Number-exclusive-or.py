class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        result = 0
        for num in nums:
            result ^= num
        return result

# 遇到相同的，则异或相消，只剩下不同的
# Beats: 99.78%
            
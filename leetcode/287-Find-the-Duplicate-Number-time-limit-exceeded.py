class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 
        n = len(nums)
        for i in range(n):
            if nums[i] in nums[i + 1: n + 1]:
                return nums[i]

# 52 / 53 test cases passed.
# Time Limit Exceeded
# medium
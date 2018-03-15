class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = -1, -1
        if target in nums:
            start = nums.index(target)
            for i in range (start, len(nums)):
                if nums[i] == target:
                    end = i
                else: break
        return [start, end]
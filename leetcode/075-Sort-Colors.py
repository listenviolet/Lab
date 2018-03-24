class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        Min, Max = min(nums), max(nums)
        count = [0] * (Max - Min + 1)
        for i in range(len(nums)):
            count[(nums[i] - Min)] += 1
        
        j = 0
        for i in range(Max - Min + 1):
            while(count[i]):
                nums[j] = Min + i
                j = j + 1
                count[i] = count[i] - 1
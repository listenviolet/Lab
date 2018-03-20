class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0

# i + nums[i] >= lastPos -> 
# assure that there is at least one step <= nums[i]
# that can reach the lastPos
# so that no need to check each one <= nums[i]
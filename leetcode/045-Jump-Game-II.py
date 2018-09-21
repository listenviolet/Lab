class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # step: 当前走的步数
        # last：step步数内可达的最远距离（也即step步数内，last距离的格子均可到达）
        # curr: step + 1 步数内可达的最远距离（step步数内可达的格子距离+该格子最远跳到的距离）
        # 当 i > last, 则step + 1, 用curr更新last
        step = 0
        last = 0
        curr = 0
        
        for i in range(len(nums)):
            if i > last: #超过了step步数内可达的最远距离，则需要步数+1到达
                last = curr
                step += 1
            curr = max(curr, i + nums[i])
        return step

# Description:
# Given an array of non-negative integers, 
# you are initially positioned at the first index of the array.

# Each element in the array represents 
# your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Note:
# You can assume that you can always reach the last index.
                
# Beats: 54.64%
# Runtime: 68ms
# hard
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        if not nums: return 0
        ans.append(nums[0])
        for i in range(1, len(nums)):
            temp = ans[i - 1] + nums[i]
            if nums[i] > temp:
                ans.append(nums[i])
            else:
                ans.append(temp)
        return max(ans)
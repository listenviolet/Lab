class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        presub = [1, 1]
        cursub = []
        M = nums[0]
        for i in range(len(nums)):
            cursub = [nums[i], nums[i] * presub[0], nums[i] * presub[1]]
            M = max(M, max(cursub))
            presub = [min(cursub),max(cursub)]
            cursub = []  # 清空数组比不清空快？
        return M

# Beats: 38.50% 
# Runtime: 53ms
# medium
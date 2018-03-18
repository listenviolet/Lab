class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub  = []
        self.dfs(nums, sub)
        return self.res
    def dfs(self, nums, subList):
        if len(subList) == len(nums):
            self.res.append(subList[:])
        for m in nums:
            if m in subList:
                continue
            subList.append(m)
            self.dfs(nums, subList)
            subList.remove(m)
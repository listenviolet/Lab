class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(nums): return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, valuelist + [nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res
# depth表示已经找好子集的前depth个元素
# 如果depth 和 nums数相等，则表示子集找完
# start表示为前depth的子集加上start位，
# 为确定部分，再寻找新子集             
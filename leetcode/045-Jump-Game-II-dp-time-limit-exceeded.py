class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minstep = [len(nums)] * len(nums)
        Max = max(nums)
        # print(minstep)
        minstep[0] = 0
        for ind in range(1, len(nums)):
            for i in range(max(0, ind - Max), ind):
                if nums[i] >= ind - i:
                    if minstep[ind] > minstep[i] + 1:
                        minstep[ind] = minstep[i] + 1
        return minstep[len(nums) - 1]
        
#         def minStep(ind):
#             if ind == 0: return 0
#             Min = len(nums)
#             for i in range(ind):
#                 if nums[i] >= ind - i:
#                     if Min > minStep(i) + 1:
#                         Min = minStep(i) + 1
#             return Min
        
#         return minStep(len(nums) - 1)

# Solution:
# minstep[ind] 表示到达ind位置需要的最小步数
# 0  1  2  3  4
# 2  3  1  1  4
# 因为nums[3] + 3 >= 4, nums[1] + 1 >= 4: 
# 即上一步在1,3 位置时均可在这一步到达ind = 4
# minstep[4] = min(minstep[3], minstep[1]) + 1

# Time Limit Exceeded
# 91 / 92 test cases passed.
# Last executed input:
# [25000,24999,24998,24997,24996,24995,24994,24993,24992,24991,
# 24990,24989,24988,24987,24986,24985,24984,24983,24982,...]
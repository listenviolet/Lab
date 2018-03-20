class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        ans = [False] * n
        ans[n - 1] = True
        if n == 1: return True
        
        
        for i in range(n - 2, -1, -1):
            if nums[i] == 0: continue
            for take in range(1, nums[i] + 1):
                if i + take > n - 1: 
                    break
                tmp = ans[i + take]
                if tmp == True: 
                    ans[i] = tmp
                    break
        return ans[0]

#Last executed input:[25000,24999,24998,24997,24996,24995,24994,24993,24992,24991,...
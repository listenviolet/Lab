class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        A = total + S
        if total < abs(S) or A % 2 == 1: return 0
        
        A //= 2
        counts = [0] * (A + 1)
        counts[0] = 1
        partial = 0
        
        nums.sort()
        
        for n in nums:
            partial += n
            for i in range(min(partial, A), n-1, -1):
                counts[i] += counts[i - n]
        return counts[A]

class Solution:  
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = int(math.sqrt(n))
        sqr = [0] * (m + 1)
        for i in range(1, m + 1):
            sqr[i] = i * i
        
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for num in range(2, n + 1):
            for i in range(m, 0, -1):
                dp[num] = min(dp[num], 1 + dp[num - sqr[i]])
        return dp[n]

# 523 / 588 test cases passed.
# Status: Time Limit Exceeded
# Last executed input: 8285
# medium
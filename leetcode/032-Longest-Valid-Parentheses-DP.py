class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        n = len(s) 
        dp = [0] * (n + 1)
        dp[-1] = 0
        for i in range (1, n):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i] == ')' and s[i - 1] == ')':
                if (i - dp[i - 1] - 1 > -1) and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        
        return max(dp)
        
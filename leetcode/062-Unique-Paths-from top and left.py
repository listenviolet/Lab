class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = [[0] * (n + 1) for _ in range (m + 1)]
        ans[1][1] = 1
        
        for i in range (1, m + 1):
            for j in range (1, n + 1):
                if ans[i][j] == 0: ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
                print(i,j,ans[i][j])
        
        return ans[m][n]
        
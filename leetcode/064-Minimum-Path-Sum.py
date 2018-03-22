class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]
        ans[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i != 0 or j != 0:
                    if i - 1 < 0 : ans[i][j] = ans[i][j - 1] + grid[i][j]
                    elif j - 1 < 0 : ans[i][j] = ans[i - 1][j] + grid[i][j]
                    else: 
                        ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + grid[i][j]
                    #print(i, j, ans[i][j])
        
        return ans[m - 1][n - 1]
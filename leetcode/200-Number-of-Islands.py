class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
    
        vis = [[0] * n for _ in range(m)]
        count = 0
    
        def visit_up(i, j):
            if i < 0: return
            if grid[i][j] == '1' and vis[i][j] == 0:
                vis[i][j] = 1
                visit_up(i - 1, j)
                visit_right(i, j +1)
                visit_down(i + 1, j)
                visit_left(i, j - 1)
            else: return
            
        def visit_right(i, j):
            if j >= n: return
            if grid[i][j] == '1' and vis[i][j] == 0:
                vis[i][j] = 1
                visit_up(i - 1, j)
                visit_right(i, j +1)
                visit_down(i + 1, j)
                visit_left(i, j - 1)
            else: return
        
        def visit_down(i, j):
            if i >= m: return
            if grid[i][j] == '1' and vis[i][j] == 0:
                vis[i][j] = 1
                visit_up(i - 1, j)
                visit_right(i, j +1)
                visit_down(i + 1, j)
                visit_left(i, j - 1)
            else: return
        
        def visit_left(i, j):
            if j < 0: return
            if grid[i][j] == '1' and vis[i][j] == 0:
                vis[i][j] = 1
                visit_up(i - 1, j)
                visit_right(i, j +1)
                visit_down(i + 1, j)
                visit_left(i, j - 1)
            else: return
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    vis[i][j] = 1
                    count += 1
                    visit_up(i - 1, j)
                    visit_right(i, j +1)
                    visit_down(i + 1, j)
                    visit_left(i, j - 1)
        return count

# Description:
# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded by water 
# and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

# Beats: 93.70%
# Runtime: 68ms
# medium      
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        row, col = 0, n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

# Solution
# 先查列，当前行的当前列若大于target，
# 则该列所在行及其下面的行的值均大于target，
# 故可以直接col -= 1 去掉

# 若matrix[row][col] < target,
# 则可以row += 1 查找
        
# Beats: 99.51%
# Runtime: 48ms
# medium
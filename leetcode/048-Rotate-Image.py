class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #上下翻 -> 中心对称翻
        if not matrix: return None
        n = len(matrix[0])
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
       
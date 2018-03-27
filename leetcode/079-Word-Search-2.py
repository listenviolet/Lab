class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, i, j, word, ind):
            if ind == len(word): return True
            if i < 0 or j < 0 or i == m or j == n: return False
            if board[i][j] != word[ind]: return False
            
            temp = board[i][j] 
            board[i][j] = '*'   # mark visited
            exist = dfs(board, i + 1, j, word, ind + 1) or dfs(board, i, j + 1, word, ind + 1) or dfs(board, i - 1, j, word, ind + 1) or dfs(board, i, j - 1, word, ind + 1)

            board[i][j] = temp  # recover to not visited
            return exist


        if not board: return False
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if(dfs(board, i, j, word, 0)): return True
        return False
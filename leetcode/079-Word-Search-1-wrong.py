def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    m = len(board)
    n = len(board[0])
    def findword0(m, n, key, row, col):
        if row >= m or col >= n:
            return -1, -1
        for i in range(col, n):
            if board[row][i] == key:
                return row, i
        if row + 1 >= m: return -1, -1
        for i in range(row + 1, m):
            for j in range(n):
                if board[i][j] == key:
                    return i, j
        return -1, -1

    def dfs(start, i, j):
        if start == len(word): return True
        flag = False
        if i + 1 < m and board[i + 1][j] == word[start] and vis[i + 1][j] == 0: 
            flag = dfs(start + 1, i + 1, j)

        elif flag == False and i - 1 >=0 and board[i - 1][j] == word[start] and vis[i - 1][j] == 0: 
            flag = dfs(start + 1, i - 1, j)
            if flag == True:
                vis[i - 1][j] == 1

        if flag == False j + 1 < n and board[i][j + 1] == word[start] and vis[i][j + 1] == 0: 
            vis[i][j + 1] == 1
            flag = dfs(start + 1, i, j + 1)
        if flag == False j - 1 >= 0 and board[i][j - 1] == word[start] and vis[i][j - 1] == 0: 
            vis[i][j + 1] == 1
            flag = dfs(start + 1, i, j - 1)
        else: return False

    row = 0
    col = 0
    I, J = findword0(m, n, word[0], row, col)

    while(I != -1 and J != -1):
        vis = [[0] * n for _ in range(m)]
        vis[I][J] = 1
        
        ans = dfs(1, I, J)
        if ans == True: return True
    return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board2 = [["a","a"]]
board3 = [["C","A","A"],["A","A","A"],["B","C","D"]]

word = "ABCCED"
word2 = "ABCB"
word3 = "SEE"
word4 = "Z"
word5 = "aaa"
word6 = "AAB"
print(exist(board2, word5))
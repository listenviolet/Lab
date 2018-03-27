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
    
    def findnext(start, i, j):
        #print("i,j: ",i, j)
        if i + 1 < m and board[i + 1][j] == word[start] and vis[i + 1][j] == 0: return i + 1, j
        elif i - 1 >=0 and board[i - 1][j] == word[start] and vis[i - 1][j] == 0: return i - 1, j
        elif j + 1 < n and board[i][j + 1] == word[start] and vis[i][j + 1] == 0: return i, j + 1
        elif j - 1 >= 0 and board[i][j - 1] == word[start] and vis[i][j - 1] == 0: return i, j - 1
        else: return -1, -1
    
    row = 0
    col = 0
    I, J = findword0(m, n, word[0], row, col)
    print(I,J)
    
    while(I != -1 and J != -1):
        vis = [[0] * n for _ in range(m)]
        vis[I][J] = 1
        flag = 1
        tmp_i, tmp_j = I, J
        
        for i in range(1, len(word)):
            print(word[i])
            ind_i, ind_j = findnext(i, tmp_i, tmp_j)
            print("ind_i, ind_j: ", ind_i, ind_j)
            if ind_i == -1 and ind_j == -1: 
                flag = 0
                break
            else:
                vis[ind_i][ind_j] = 1
                tmp_i = ind_i
                tmp_j = ind_j
        if flag: return True
        elif flag == 0: 
            row = I + (J + 1) // 4
            col = (J + 1) % 4
            I, J = findword0(m, n, word[0], row, col)
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
print(exist(board, word6))

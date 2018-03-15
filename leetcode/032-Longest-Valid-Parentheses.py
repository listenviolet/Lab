def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    def isValid(i, j):
        if s[i] == '(' and s[j] == ')': return True
        else: return False
        
    #Init  
    maxlen = 0
    for i in range (0, n - 1):
        if isValid(i, i + 1):
            dp[i][i + 1] = True
            maxlen = 2

    for i in range (n - 4, -1, -1):
        for j in range (i + 3, n):
            dp[i][j] = isValid(i, j) and dp[i + 1][j - 1] 
            if dp[i][j] == False: 
                for k in range (i + 1, j - 1):
                    dp[i][j] = dp[i][k] and dp[k + 1][j]
                    if dp[i][j] == True: break
            #print("(",i,",",j,"): ", dp[i][j])
            if dp[i][j] == True and (j - i + 1 > maxlen):
                maxlen = j - i + 1
    return maxlen

s = ")(((((()())()()))()(()))("
s2 = "(()())"
maxlen = longestValidParentheses(s)
print(maxlen)

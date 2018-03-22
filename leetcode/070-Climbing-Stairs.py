def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    ans = [0] * (n + 1)
    ans[0] = 1
    ans[1] = 1
    for i in range(2, n + 1):
        ans[i] = ans[i - 1] + ans[i - 2]
    
    return ans[n]

print(climbStairs(3))
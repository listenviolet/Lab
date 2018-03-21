class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from math import factorial
    
        N = m - 1 + n - 1
        k = m - 1
        num = factorial(N)
        den = factorial(N - k) * factorial(k)
        return num // den
#total steps : N
#choose m - 1 : go down -> C(N, k) = C(N, N - k)
def expendAroundCenter(s, L, R):
    n = len(s)
    while L >= 0 and R < n and s[L] == s[R]:
        L = L - 1
        R = R + 1
    return R - L - 2
    
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        start = 0
        end = 0
        for i in range(0,n):
            len1 = expendAroundCenter(s, i, i)
            len2 = expendAroundCenter(s, i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > (end - start):
                start = i - maxlen // 2
                end = i + (maxlen + 1) // 2
        return s[start:(end + 1)]
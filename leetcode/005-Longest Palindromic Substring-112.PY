class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(s):
            return s == s[::-1]

        if len(s) == 0:
            return 0

        # a single character is a palindrome of length=1
        max_len = 1
        start_ind = 0
        for i in range(len(s)):
            # only test for palindromes of length max_len+1 and max_len+2
            # cannot be max_len+3 (or more) otherwise a palindromic substring
            # would be present ending in the previous character which would have
            # length > max_len -> violating condition that max_len is the longest
            # palindrome up to current point
            if i - max_len >= 1 and is_palindrome(s[i - max_len - 1:i + 1]):
                start_ind = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and is_palindrome(s[i - max_len:i + 1]):
                start_ind = i - max_len
                max_len += 1
        return s[start_ind:start_ind + max_len]
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = 0
        for center in range(2 * N):
            left = center // 2
            right = left + center % 2
            
            while left >=0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

# Description:
# Given a string, your task is to count 
# how many palindromic substrings in this string.

# The substrings with different start indexes 
# or end indexes are counted as different substrings 
# even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.

# Solution:
# https://leetcode.com/problems/palindromic-substrings/solution/
# Approach #1: Expand Around Center [Accepted]
# Intuition

# Let N be the length of the string. The middle of the palindrome could be in one of 2N - 1 positions: either at letter or between two letters.

# For each center, let's count all the palindromes that have this center. Notice that if [a, b] is a palindromic interval (meaning S[a], S[a+1], ..., S[b] is a palindrome), then [a+1, b-1] is one too.

# Algorithm

# For each possible palindrome center, let's expand our candidate palindrome on the interval [left, right] as long as we can. The condition for expanding is left >= 0 and right < N and S[left] == S[right]. That means we want to count a new palindrome S[left], S[left+1], ..., S[right].

#         c
#         |
# 0 1 2 3 4 5 6 7 8 9
#     |
#  <-l,r->

#           c
#           |
# 0 1 2 3 4 5 6 7 8 9
#     | |
#   <-l r->

# Complexity Analysis

# Time Complexity: O(N^2) where NN is the length of S. 
# Each expansion might do O(N)work.

# Space Complexity: O(1).

# Beats: 89.26%
# Runtime: 116ms
# medium
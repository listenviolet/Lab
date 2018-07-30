class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manachers(S):
            T = '@#' + '#'.join(S) + '#$'
            P = [0] * len(T)
            center = right = 0
            
            for i in range(1, len(T) - 1):
                if i < right:
                    P[i] = min(right - i, P[2 * center - i])
                while T[i + P[i] + 1] == T[i - P[i] - 1]:
                    P[i] += 1
                if i + P[i] > right:
                    center, right = i, i + P[i]
            return P
        return sum((p + 1) // 2 for p in manachers(s))

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
# Approach #2: Manacher's Algorithm [Accepted]

# Complexity Analysis

# Time Complexity: O(N) where N is the length of S. 
# As discussed above, the complexity is linear.

# Space Complexity: O(N), the size of T and P.

# Note:
# Manacher算法讲解：
# https://www.cnblogs.com/egust/p/4580299.html
# 主要分三种情况
# 1. i > right; -- 超出之前的回文串范围，所以从n = 0重新开始找
# 2. P[mirror] <= right - i; --在之前的回文串范围内-取对称位置的P[mirror]
# 3. i <= right and P[mirror] > right - i; 
# --P[i]取在回文串范围内的部分长度，超出的部分从right + 1重新比较

# Beats: 98.09%
# Runtime: 48ms
# medium

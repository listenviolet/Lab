class Solution:
    def findAnagrams(self, s, p):
        start = 0
        res = []
        cache = collections.defaultdict(int)
        for ch in p: cache[ch] += 1
        for i, ch in enumerate(s):
            if ch in cache:
                cache[ch] -= 1
                while cache[ch] < 0:
                    cache[s[start]] += 1
                    start += 1
                if cache[ch] == 0 and i - start == len(p) - 1:
                    res.append(start)
            else:
                while start <= i:
                    if s[start] in cache:
                        cache[s[start]] += 1
                    start += 1
        return res

# Description:
# Given a string s and a non-empty string p, 
# find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only 
# and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", 
# which is an anagram of "abc".
# The substring with start index = 6 is "bac", 
# which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", 
# which is an anagram of "ab".
# The substring with start index = 1 is "ba", 
# which is an anagram of "ab".
# The substring with start index = 2 is "ab", 
# which is an anagram of "ab".

# 最佳答案
# 没看懂
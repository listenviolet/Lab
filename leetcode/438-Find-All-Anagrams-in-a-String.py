class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        if s is None or p is None: return ans
        set_p = set(p)
        len_s, len_p = len(s), len(p)
        tmp = s[:len_p]
        counter_tmp = collections.Counter(tmp)
        counter_p = collections.Counter(p)
        for i in range(len_s - len_p + 1):
            flag = 1
            
            for item in set_p:
                if counter_tmp[item] != counter_p[item]:
                    flag = 0
                    break
            if flag == 1:
                ans.append(i)
            if i < len_s - len_p:
                counter_tmp.update([s[i + len_p]])
                counter_tmp.subtract([s[i]])
        return ans

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

# Solution:
# 每次比较set_p的counter与从s中截取的len_p长度的list中counter
# 如果对于set_p中每一个元素，在p,tmp的counter中均相同，
# 则这段匹配。

# 这里不是直接用的每段tmp的counter，
# 而是利用update和subtract，每次添加后一位，去除第一位。
# 否则，对于遍历的每一位直接用counter，会超时。

# Beats: 6.60%
# Runtime: 668ms
# easy
        
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s: return 0
        start, end, Max = 0, 0, 0
        subs = []
        while end < len(s):
            if s[end] not in subs:
                subs.append(s[end])                          
            else:
                start += subs.index(s[end]) + 1
                subs = list(s[start : end + 1])
            Max = end - start + 1 if end - start + 1 > Max else Max
            end += 1
        return Max
                
# Description
# Given a string, find the length of the longest substring 
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, 
# "pwke" is a subsequence and not a substring.

# Solution:
# 用start, end 标记当前判别的子序列的起始与终止index。
# 若当前序列s[start: end + 1] 没有重复字符，
# 更新Max, 并 end + 1 
# 若当前新加入的s[end]与之前的子串subs中某元素重复，
# 则定位subs中重复元素的index, 
# 更新start为该index + 1，并更新subs.
# 依此规则，每一次end后移(+1)，则进行一次判断并更新。
# 最终Max即为所求最长无重复子串长度。

# Note:
# subs = list(s[start : end + 1])
# 这里若直接subs = s[start : end + 1]，则subs为str类型，
# 需要转为list类型，即将str按字母元素分隔开。
# eg. “abc” -> 'a','b','c'

# Note:
# 因为subs中即为无重复子串，则无需用set, 
# 可直接通过判断新加入的s[end]是否在subs中，来判断是否有重复字符

# Beats：35.65%
# Runtime: 124ms
# medium

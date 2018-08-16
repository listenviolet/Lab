class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {}
        maxlength = 0
        count = 0
        start = 0
        for index, i in enumerate(s):
            if i in d and d[i] >= start:
                count = index - d[i]
                start = d[i]
            else:
                count+=1
            d[i] = index
            if count>maxlength:
                maxlength = count
            
        return maxlength

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
# 这里复制了leetcode上最快的答案
# 
# 解法中用到了dict: d
# i:字母元素 d[i]: 更新后的字母元素在s中的index 
#
# -> 每当遍历新的s元素，更新该元素在d中的映射值 
# (新元素：添加；已有元素：更新)
# 这样可以直接定位到其index, 而不需要每次通过s.index()查找
#
# index表示当前遍历到的s中元素的ind
# start表示当前子串的起始ind
# count表示当前子串的长度

# Beats: 99.93%
# Runtime: 68ms
# medium
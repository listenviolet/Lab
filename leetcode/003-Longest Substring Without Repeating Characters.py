class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        longestlength = 1
        substr = ""
        for item in s:
            if item not in substr:
                substr += item
            else:
                if len(substr) > longestlength:
                    longestlength = len(substr)
             
                #将重复字符加入substr
                substr += item
                # 应该从substr中第一次出现重复字符的下一个字符开始继续判断
                substr = substr[substr.index(item) + 1:]
        
        if len(substr) > longestlength:
            longestlength = len(substr)
        return longestlength

# Description
# Given a string, find the length of the longest substring 
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, 
# "pwke" is a subsequence and not a substring.

# Beats: 44.09%
# Runtime: 108ms
# medium
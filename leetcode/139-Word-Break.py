class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordB = [False] * (n + 1)
        wordB[0] = True
        
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if wordB[j] and s[j: i] in wordDict:
                    wordB[i] = True
                    break
        return wordB[-1]

# Question:
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

# Solution:

# 题目意思是，给定词典的情况下，看看原字符串能不能全部成功地被给定的词典分割。一开始，最自然的想法是，使用递归。提交，超时了。
# 想想，这个问题其实具有动态规划的特点。比如计算catsanddog的分割方式，那么倒着想如下：
# 到了最后一个字符g的时候，
# 如果能在g之前切一刀，也就是说，如果g在词典中以及catsanddo能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在og之前切一刀，也就是说，如果og在词典中以及catsandd能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在dog之前切一刀，也就是说，如果dog在词典中以及catsand能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在ddog之前切一刀，也就是说，如果ddog在词典中以及catsan能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在nddog之前切一刀，也就是说，如果nddog在词典中以及catsa能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在anddog之前切一刀，也就是说，如果anddog在词典中以及cats能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在sanddog之前切一刀，也就是说，如果sanddog在词典中以及cat能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在tsanddog之前切一刀，也就是说，如果tsanddog在词典中以及ca能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在atsanddog之前切一刀，也就是说，如果atsanddog在词典中以及c能够成功切分，那么原字符串就可以成功切分。
# 或者，如果能在catsanddog之前切一刀，也就是说，如果catsanddog在词典中以及""能够成功切分，那么原字符串就可以成功切分。
# 使用一个数组bool wordB[i] 来记录，在单词长度为i的时候，能否成功切分(i取值范围必然为[ 0, word.length() ] )

# DP
# Beats: 98.42%
# Medium
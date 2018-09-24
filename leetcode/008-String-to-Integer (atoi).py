class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def isNum(ch):
            if ch >= '0' and ch <= '9':
                return True
            else: return False
        
        def overMax(ans, Max):
            if len(ans) > len(Max): return True
            elif len(ans) < len(Max): return False
            else:
                for i in range(len(ans)):
                    if ans[i] > Max[i]: return True
                    elif ans[i] < Max[i]: return False
                return True
            
        def list2int(ans):
            if not ans: return 0
            ret = ans[0]
            i = 1
            while i < len(ans):
                ret = ret * 10 + (ans[i])
                i += 1
            return ret
        
        start = 0
        if not str: return 0
        
        while start < len(str) and (str[start] == ' '):
            start += 1
        
        if start >= len(str): return 0
        
        if str[start] != '-' and str[start] != '+' and isNum(str[start]) == False:
            return 0
        
        flag = 1
        if start < len(str) and str[start] == '-': 
            start += 1
            flag = -1
        elif start < len(str) and str[start] == '+':
            start += 1
            
        ans = []
        while start < len(str) and str[start] == '0':
            start += 1
        while start < len(str) and isNum(str[start]) == True:
            ans.append(ord(str[start]) - ord('0'))
            start += 1
        # print(ans)
        if flag == 1: # 2147483647
            Max = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
            if overMax(ans, Max) == True: return 2147483647
            else: return list2int(ans)
        if flag == -1: #-2147483648
            Max = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
            if overMax(ans, Max) == True: return -2147483648
            else: return -1 * list2int(ans)

# Description:
# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary 
# until the first non-whitespace character is found. 
# Then, starting from this character, 
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
# and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, 
# which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, 
# or if no such sequence exists because either str is empty or it contains only whitespace characters, 
# no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment 
# which could only store integers within the 32-bit signed integer range: 
# [−2^31,  2^31 − 1]. 
# If the numerical value is out of the range of representable values, 
# INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:

# Input: "42"
# Output: 42
# Example 2:

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', 
# which is the minus sign.
# Then take as many numerical digits as possible, 
# which gets 42.
# Example 3:

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. 
# Therefore no valid conversion could be performed.
# Example 5:

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
# Thefore INT_MIN (−2^31) is returned.

# Solution:
# 注意几个例子：
# 0000000000001
# +01
# -+1
# 0-1

# 所以应先去空格，再判断+-，再消0，再转为数组存储
# python没有字符串相减的操作，故用ord(ch1) - ord(ch2)

# Beats: 58.32%
# Runtime: 68ms
# medium
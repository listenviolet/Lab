class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        rev = 0
        flag = 1
        if x < 0: 
            flag = -1
            x *= -1
        INT_MAX = 2147483647
        INT_MIN = 2147483648
        
        if flag > 0:
            while x > 0:
                pop = x % 10
                x = x // 10
                if rev > (INT_MAX // 10) or (rev == INT_MAX // 10 and pop > 7): return 0
                rev = rev * 10 + pop

        if flag < 0:
            while x > 0:
                pop = x % 10
                x = x // 10  
                if rev > (INT_MIN // 10) or (rev == INT_MIN // 10 and pop > 8): return 0
                rev = rev * 10 + pop
        return flag * rev

# Description:
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
# For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.

# Solution:
# https://leetcode.com/problems/reverse-integer/solution/
# 每次直接使用pop的值，避免了开数组空间

# Notice:
# 1. python的负数取余运算与c的不同：
#     C语言向0取整，python向负无穷取整。
#     (-17) mod 5 =?
#     答案一： (-17) = (-3)*5 + (-2)，所以余数是 -2 。（C语言）
#     答案二： (-17) = (-4)*5 + (+3)，所以余数是 +3 。（python）

#     所以自己在写的时候，分了+-两种情况讨论。
# 2. integer的范围：
#     [-2147483648, 2147483647]
#     最后一位一个是8，一个是7
#     在进行是否越界的判断时，有所不同。
            
# Beats: 99.93%
# Runtime: 52ms
# easy
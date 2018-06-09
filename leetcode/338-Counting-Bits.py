class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = 0
        tmp = num
        while(tmp // 2 > 0):
            count += 1
            tmp = tmp // 2
        
        res = num - pow(2, count)
        
        a = [0] * (num + 1)
        a[0] = 0
        if num > 0:
            a[1] = 1
        if num >= 2:
            for i in range(1, count):
                for j in range(pow(2, i)):
                    a[pow(2, i) + j] = 1 + a[j]
            last = pow(2, count)      
            for i in range(res + 1):
                a[last + i] = 1 + a[i]
        return a 

# Description:
# Given a non negative integer number num. 
# For every numbers i in the range 0 ≤ i ≤ num 
# calculate the number of 1's in their binary representation 
# and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution 
# with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? 
# Do it without using any builtin function 
# like __builtin_popcount in c++ or in any other language.   

# Solution:
# 0: 1
# 1: 1
# --------
# 2:  1 << 1 + a[0] : 1 + a[0]
# 3:  1 << 1 + a[1] : 1 + a[1]
# --------
# 4:  1 << 2 + a[0] : 1 + a[0]
# 5:  1 << 2 + a[1] : 1 + a[1]
# 6:  1 << 2 + a[2] : 1 + a[2]
# 7:  1 << 2 + a[3] : 1 + a[3]
# --------
# 8:  1 << 3 + a[0] : 1 + a[0]
# 9:  1 << 3 + a[1] : 1 + a[1]
# 10: 1 << 3 + a[2] : 1 + a[2]
# 11: 1 << 3 + a[3] : 1 + a[3]
# 12: 1 << 3 + a[4] : 1 + a[4]
# ...
# 15: 1 << 3 + a[7] : 1 + a[7]
# ...

# for 12:
#     12 = pow(2, 3) + 4
#                 |    |
#               count res


# Beats: 65.41%
# Runtime: 124ms
# medium
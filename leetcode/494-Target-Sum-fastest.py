class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        A = total + S
        if total < abs(S) or A % 2 == 1: return 0
        
        A //= 2
        counts = [0] * (A + 1)
        counts[0] = 1
        partial = 0
        
        nums.sort()
        
        for n in nums:
            partial += n
            for i in range(min(partial, A), n-1, -1):
                counts[i] += counts[i - n]
        return counts[A]

# Solution:
# 以下是对从leetcode accepted solution中
# 选取的best solution的解释
#
# 1.A的意义：
# total 为nums之和
# A = total + S 
# o o o o o
# - + + + -
# | | | | |
# 0 2 2 2 0
#
# 由此可见，A为偶数并且total < |S| 时有解
# A = A // 2 即为正数之和
# 如题目样例：
# 1 1 1 1 1
# - + + + +
#
# A = total + S = 5 + 3 = 8
# A = A // 2 = 8 // 2 = 4
# 这里取+的nums的和为4
##########################################################

# 2. counts的意义：
# counts[i]表示取正数的nums之和为i的可能的组合数/情况
# 例如counts[4] = 5
# 表示有5种不同的+-组合可以使取整数的nums之和为4（本题样例）
#
# 所以本方法将题目直观的 
# 欲求解有多少种+-组合情况使nums之和为S
# 转换为 有多少种组合情况使nums中取+的数之和为A
# 这样只需考虑+的情况，而无需考虑-的情况了
##########################################################

# 3. 主要算法--遍历更新的意义：
# 重点是对counts的更新
# 每遍历到nums中一个新的n:

# i 的遍历范围为[min(partial, A), n]
#
# 这里partial为每次遍历到的n的值之和，
# 即为遍历到当前n，nums取+的数值之和最大即为所有n均取+，
# 即partial += n
# 而题目要求，nums取+的数值之和最大为A,
# 故i的最大值应取min(partial, A)
#
# 最小即为遍历到n，之前均取-，nums取+的数值之和为当前n值

# 新的counts[i] 的值为老的counts[i] 的值 + counts[i - n]
# 因为当前搜到数字n, 
# counts[i - n] 表示正数之和为(i - n)的组合数
# 即为如果加上当前搜索到的n可以达到i的组合数
# 也即对counts[i]的更新的部分

# Beats: 99.59%
# Runtime: 60ms
# medium
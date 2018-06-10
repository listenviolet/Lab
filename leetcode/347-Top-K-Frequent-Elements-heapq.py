class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res = {}, []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        
        return heapq.nlargest(k, data, key = lambda x: data[x])

# Description:
# Given a non-empty array of integers, 
# return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size.

# Solution:
# 这里利用了python的heapq函数，关于该函数：
# https://blog.csdn.net/minxihou/article/details/51857518
#
# nlargest(n , iterbale, key=None) 
# 从堆中找出做大的N个数，
# key的作用和sorted( )方法里面的key类似，
# 用列表元素的某个属性和函数作为关键字。
# eg.
# >>>a = [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
# >>>heapq.nlargest(5,a)
# [25, 20, 15, 10, 8]
#
# eg.
# >>>b = [('a',1),('b',2),('c',3),('d',4),('e',5)]
# >>>heapq.nlargest(1,b,key=lambda x:x[1])
# [('e', 5)]
#
# nsmallest(n, iterable, key=None) #找到堆中最小的N个数用法同上。

# Beats: 99.13%
# Runtime: 48ms
# medium
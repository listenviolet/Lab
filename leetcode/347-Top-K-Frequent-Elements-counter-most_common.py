class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return [item[0] for item in counter.most_common(k)]

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
# 这里利用了python的标准库——collections模块的Counter类
# 对该类的详解，见：
# http://www.pythoner.com/205.html
# eg.
# >>> c = Counter("abcdefgab")
# >>> c["a"]
# 2
# >>> c["c"]
# 1
# >>> c["h"]
# 0
# 
# eg.
# most_common([n]):
# 返回一个TopN列表。如果n没有被指定，则返回所有元素。
# 当多个元素计数值相同时，排列是无确定顺序的。
# >>> c = Counter('abracadabra')
# >>> c.most_common()
# [('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
# >>> c.most_common(3)
# [('a', 5), ('r', 2), ('b', 2)]


# Beats: 99.13%
# Runtime: 48ms
# medium
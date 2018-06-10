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
        sorted_data = sorted(data.items(), key = operator.itemgetter(1), reverse = True)
        for i in range(k):
            res.append(sorted_data[i][0])
        return res

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
# 这里思路是有的，在写python代码时，注意
# set的写法：
# data[i] = data[i] + 1 if i in data else 1
# 
# 和对set按照键值对中的值从大到小排序的写法：
# sorted_data = sorted(data.items(), key = operator.itemgetter(1), reverse = True)


# Beats: 94.43%
# Runtime: 52ms
# medium
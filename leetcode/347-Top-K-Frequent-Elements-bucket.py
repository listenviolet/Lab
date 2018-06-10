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
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key in data:
            bucket[data[key]].append(key);
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]
        
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
# 这里将之前的sorted换为了桶排序
# 这里将每一个数字出现的次数作为桶的序号：
# bucket[i] = [j,k,...]
# 的意义为数字j, k, ... 都出现了i次
# 那么bucket的序号本身就是对数字出现次数的排序
# 从len(bucket) - 1开始向前，依次将bucket[i]不为空的元素拿到res数组中，
# res即为前k个最常出现的元素数组。
# 桶排序：O(n)

# Beats: 40.87%
# Runtime: 64ms
# medium

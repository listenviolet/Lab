class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        for val in nums:
            if count == 0:
                candidate = val
            if candidate == val:
                count += 1
            else:
                count -= 1
        return candidate

# Solution:
# Boyer-Moore 算法
# 该算法时间复杂度为O(n)，空间复杂度为O(1)，
# 只需要对原数组进行两趟扫描，并且简单易实现。
# 第一趟扫描我们得到一个候选节点candidate，
# 第二趟扫描我们判断candidate出现的次数是否大于⌊ n/2 ⌋。

# 第一趟扫描中，我们需要记录2个值：
# 1. candidate，初值可以为任何数
# 2. count，初值为0

# 之后，对于数组中每一个元素，首先判断count是否为0，
# 若为0，则把candidate设置为当前元素。
# 之后判断candidate是否与当前元素相等，
# 若相等则count+=1，否则count-=1。

# 在第一趟扫描结束后，如果数组中存在多数元素，那么candidate即为其值，
# 如果原数组不存在多数元素，则candidate的值没有意义。
# 所以需要第二趟扫描来统计candidate出现的次数来判断其是否为多数元素。

# Beats: 91.20%
# Runtime: 52ms
# easy
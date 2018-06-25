class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        if not nums: return ans
        nums.sort()
        nums = [0] + nums[:]
        # print(nums)
        count = 1
        for i in range(1, len(nums)):
            # print(nums[i], count)
            while(nums[i] != count and nums[i] != nums[i - 1]):
                ans.append(count)
                count += 1
            if(nums[i] == nums[i - 1]):
                continue
            count += 1
        last = nums[-1]
        while(last + 1 < len(nums)):
            ans.append(last + 1)
            last += 1
        return ans

# Description:
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive 
# that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

# Solution:
# 首先排序
# count用于计数1-n
# 认为与前一位不同的nums[i],为一个有效位
# 如果当前位与count不同并且当前位与前一位不同，
# 则表明这一位与count之间有数值差，需要将差的数值补在ans中。

# 如果nums[i] == nums[i - 1]，
# 则该位不是有效位，应跳过该位，count值保持不变，continue循环。

# 每比较完一次有效位，count值自增1.

# Note:
# 另外需要注意点是
# 对于测试样例： [1, 1] [2]
# 需保证nums.sort()后的最后一位数值为原数组长度。
# 上文所示算法，均为保证了最大值即为原数组长度，
# 在中间空缺的地方补值

# 而对于最大值小于原数组长度的，应补上[nums[-1] + 1 : len(nums)]这段
# 可以将上述代码的while循环换为：
# ans = ans + [i for i in range(nums[-1] + 1, len(nums))] 
# 替换后：
# Beats: 25.00%  Runtime: 260ms

# Beats: 24.18%
# Runtime: 264ms
# easy
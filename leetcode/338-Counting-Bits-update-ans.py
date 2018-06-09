class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) < num + 1:
            ans += [1 + x for x in ans]
        # len(ans) > num
        return ans[:num+1]

# Solution:
# 大体思路和自己的一样
# 但是 1本身也是 1 + 前一个unit的 0
# 每次都是 1 + 前一个unit的每一项
# 这样可以每次更新ans,
# 每次的ans都是计算完这个unit之后的结果

# Beats: 99.78%
# Runtime: 104ms
# medium
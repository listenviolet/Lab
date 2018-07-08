class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def dec2bin(num):
            l = []
            while True:
                num, remainder = divmod(num, 2)
                l.append(remainder)
                if num == 0:
                    return l
        bin_x = dec2bin(x)
        bin_y = dec2bin(y)
        # print(bin_x, bin_y)
        diff = 0

        flag = 0 if len(bin_x) < len(bin_y) else 1

        for i in range(min(len(bin_x), len(bin_y))):
            if bin_x[i] != bin_y[i]:
                diff += 1

        if flag == 0:
            for i in range(len(bin_x), len(bin_y)):
                if bin_y[i] == 1:
                    diff += 1
        else:
            for i in range(len(bin_y), len(bin_x)):
                if bin_x[i] == 1:
                    diff += 1

        return diff


# Description:
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#     ↑   ↑

# The above arrows point to positions w
# here the corresponding bits are different.

# Solution:
# from dec to bin:
# use function: divmod(num, 2) to get the quotient and remainder
# then compare each tf.bits

# Note:
# for the longer one, count the number of 1 in the last part of l,
# not the length of(max(l1, l1) - min(l1, l2)).

# Beats: 100.00%
# Runtime: 36ms
# easy

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

# The popitem()

# returns an arbitrary element (key, value) pair from the dictionary
# removes an arbitrary element (the same element which is returned) from the dictionary.

# Beats: 70.23%
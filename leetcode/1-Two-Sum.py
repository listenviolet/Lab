class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_num = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp_num:
                return (tmp_num[target - nums[i]], i)
            else:
                tmp_num[nums[i]] = i;
        return (-1, -1)
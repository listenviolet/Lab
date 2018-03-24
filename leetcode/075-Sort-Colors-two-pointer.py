class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        head, tail, i = 0, len(nums) - 1, 0
        while i <= tail:
            if nums[i] == 0:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1  #no need to i += 1, the [i] is needed to be judeged
def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n == 0: return None
    else:
        flag = 1
        for i in range (n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                flag = 0
                for j in range (n - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        break
                tmp = nums[i:n]
                tmp.sort()
                nums[i:n] = tmp
                break
        if flag == 1: nums.reverse()

nums = [1,3,2]
nextPermutation(nums)
print(nums)

#1 2 4 3
#找到第一个[i - 1] < [i] 的，
#从[i:n]中找到第一个大于[i - 1]的[j]
#（由于已经字典序，故逆序找即可），
#将[i - 1] 与[j]交换， 
#再对[i:n]按顺序排列即可
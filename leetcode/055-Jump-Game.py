def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def move(left, i):
        if left == 0 and i == len(nums) - 1: return True
        elif i >= len(nums) - 1 and left != 0: return False
        
        for take in range(nums[i], 0, -1):
            res = move(left - take, i + take)
            if res == True: return True
            else: continue
        return False
    
    return move(len(nums) - 1, 0)

nums = [3,2,1,0,4]
nums2 = [2,3,1,1,4]
nums3 = [2, 0]
print(canJump(nums2))
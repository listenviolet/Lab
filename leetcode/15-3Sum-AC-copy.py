class Solution:
   
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                j = i + 1
                k = len(nums) - 1
                
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    
                    if sum == 0:
                        res.add((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1
        
        return list(res)
    
        #固定i,移动j,k
        #用set消除重复
        #最后list(res) 转换为list
             
            
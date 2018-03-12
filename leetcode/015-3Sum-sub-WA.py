def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        #print(nums)
        memo = {}
        memo_nums = {}
        def func(l, r):
            #print("l:",l,"r:", r)
            if l < r - 1 and nums[l] <= 0 and nums[r] >= 0:
                #print("(",l, r,") --", memo)
                if (l, r) not in memo and (nums[l], nums[r]) not in memo_nums:
                    target = 0 - nums[l] - nums[r]
                    tmp = nums[l + 1: r]
                    #print("l:",l,"r:", r, "tmp: ", tmp)

                    if target not in tmp:
                        memo[l, r] = False
                        
                        if target < nums[l]: func(l, r - 1)
                        elif target > nums[r]: func(l + 1, r)
                        else:
                            func(l + 1, r)
                            func(l, r - 1)
                    else:
                        memo[l, r] = True
                        memo_nums[nums[l], nums[r]] = True
                        if [nums[l], target, nums[r]] not in ans:
                            ans.append([nums[l], target, nums[r]])

                        func(l + 1, r)
                        func(l, r - 1)
                    #print("memo:", memo)  
                else:
                    func(l + 1, r)
                    func(l, r - 1)
        func(0, len(nums) - 1)
        return ans

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#nums = [-4,-2,-2,0,1,2,2,3,3,4,6]
print(threeSum(nums))
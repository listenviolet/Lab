def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combine(candidates, target, curr):
            if target == 0:
                ans.append(curr[:]) #!!![:] 表示数组全部元素，不可以只写curr!
                return
            else:
                n = len(candidates)
                for i in range (n):
                    if target < candidates[i]: return
                    curr.append(candidates[i])
                    combine(candidates[i:n], target - candidates[i], curr)
                    curr.pop()
     
        ans = []
        tmp_candidates = candidates
        tmp_target = target
        tmp_ans = []
        
        combine(tmp_candidates, tmp_target, tmp_ans)
        return ans

candidates = [2, 3, 6, 7]
target = 6
print(combinationSum(candidates, target))
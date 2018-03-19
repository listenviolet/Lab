class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans, res, ret  = [], {}, []
        for s in strs:
            temp = list(s)
            temp.sort()
            ans.append("".join(temp))
        
        for i in range(len(ans)):
            if ans[i] not in res:
                res[ans[i]] = []
            res[ans[i]].append(strs[i])
        
        for key in res:
            ret.append(res[key])
        
        return ret
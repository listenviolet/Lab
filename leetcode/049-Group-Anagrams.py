def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []

        def sort_str(str):
            if str:
                l = list(str)
                l.sort()
                str = "".join(l)
            return str

        def search(strs, key, sub):
            #for i in range(len(strs)):
            i = 0
            while(i < len(strs)):
                print("strs:", strs)
                if key == sort_str(strs[i]):
                    sub.append(strs[i])
                    del strs[i]
                    i = i - 1
                i = i + 1
            return sub, strs

        while(strs):                                               
            key = sort_str(strs[0])
            sub = []
            sub, strs = search(strs, key, sub)
            ans.append(sub)

        return ans



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = ["",""]
print(groupAnagrams(strs2))


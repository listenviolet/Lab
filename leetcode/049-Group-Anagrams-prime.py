def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103];  

    ans = {}
    ret = []
    for s in strs:    	
    	temp = 1
    	for j in range(len(s)):
    		print(s[j])
    		temp = temp * primes[(ord(s[j]) - ord('a'))]
    	if temp not in ans:
    		ans[temp] = []
    	ans[temp].append(s)

    for key in ans:
    	ret.append(ans[key])
    return ret

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = ["", ""]
print(groupAnagrams(strs2))
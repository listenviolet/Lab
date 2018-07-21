def leastInterval(tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        dic = {}
        l = len(tasks)
        for i in range(l):
            if tasks[i] not in dic:
                dic[tasks[i]] = 1
            else:
                dic[tasks[i]] += 1
        dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
        ans = l
        while dic:
            dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
            print(dic)
            count = 0
            dellist = []
            key = '0'
            for i in dic:
                count += 1
                if count > 1:
                    break
                key = i
                
            dic[key] -= 1
            cur_n = n

            for j in dic:
                if j != key and dic[j] > 0 and cur_n > 0:
                    dic[j] -= 1
                    cur_n -= 1

            for check in dic:
                if dic[check] == 0:
                    dellist.append(check)
        
            for delitem in dellist:
                dic.pop(delitem)
            if dic:
                ans += cur_n
                    
        return ans

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(leastInterval(tasks, n))
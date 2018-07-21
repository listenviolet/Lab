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

# 自己测试是正确的，但是提交时显示的结果每次是随机的

# Description:
# Given a char array representing tasks CPU need to do. 
# It contains capital letters A to Z 
# where different letters represent different tasks.
# Tasks could be done without original order. 
# Each task could be done in one interval. 
# For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n 
# that means between two same tasks, 
# there must be at least n intervals 
# that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals 
# the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

# Solution:
# 转成dict，每次按任务数从大到小从dict中取任务
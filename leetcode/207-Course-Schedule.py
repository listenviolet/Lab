class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses  # 入度数
        childs = [[] for x in range(numCourses)] # 每一门课的后继课list
        for pair in prerequisites:
            degrees[pair[0]] += 1 # 后继节点入度数+1
            childs[pair[1]].append(pair[0]) #child[前驱] = [后继1，后继2,...]
        
        courses = set(range(numCourses))
        flag = True
        
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:  #入度为0，即没有前驱节点
                    for child in childs[x]:
                        degrees[child] -= 1  #删除与之相连的后继节点
                    removeList.append(x)     #将该前驱节点添加到removeList中
                    flag = True           #存在入度为0的，flag置为True
            for x in removeList:
                courses.remove(x)          #从courses中删去该前驱课程
        return len(courses) == 0           #若为空，则无环，说明可以；
                                           #若不存在没有前驱节点的节点，则有环，不可以
# Description:
# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
#  Hints:

# This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.

# Solution:
# DFS:
# L ← Empty list that will contain the sorted nodes
# S ← Set of all nodes with no outgoing edges
# for each node n in S do
#     visit(n) 
# function visit(node n)
#     if n has not been visited yet then
#         mark n as visited
#         for each node m with an edgefrom m to ndo
#             visit(m)
#         add n to L

# Beats: 35.12%
# Runtime: 92ms
# medium

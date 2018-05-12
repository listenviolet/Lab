class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y) # x的前驱是y
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1: return False
        
        # if it is done visted, then do not visit again
        if visited[i] == 1: return True
        
        # mark as being visited
        visited[i] = -1
        
        # 访问前驱节点
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
            
        #访问完所有前驱节点，标记为done visited
        visited[i] = 1
        return True

# Beats: 99.27%
# Runtime: 48ms
# medium
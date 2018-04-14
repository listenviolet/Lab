class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [0] * (n + 1)
        s[0] = 1
        s[1] = 1
        
        def S(N):
            for n in range(N + 1):
                if s[n] == 0:
                    for i in range(n):
                        s[n] = s[n] + s[i] * s[n - i - 1]
            return s[n]
        return S(n)

# Q: Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# Solution:
# 对于序列1,2，... i,..., N
# 依次选取 1, 2, ..., N作为树根
# 根据中序特点，若取i作为root, 
# 则比i小的数的集合构成左子树
# 比i大的数的集合构成右子树
# 左右子树的构建方法同该树的构建方法
# 树BST总数 = sum(左子树的BST总数 * 右子树BST总数)
# s[N] = sum(s[n = i] * s[n = N - i - 1]) for i: [0, N)
# 其中N表示整个树的节点总数；
# n表示子树节点总数，空节点用 n = 0表示
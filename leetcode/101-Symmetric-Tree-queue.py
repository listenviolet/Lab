# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = []
        q.append(root)
        q.append(root)
        while(q):
            t1 = q.pop()
            t2 = q.pop()
            if t1 is None and t2 is None: continue
            if t1 is None or t2 is None: return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

# Use iteration with the aid of a queue. 
# Each two consecutive nodes in the queue should be equal, 
# and their subtrees a mirror of each other. 
# Initially, the queue contains root and root. 
# Then the algorithm works similarly to BFS, 

# with some key differences. 
# Each time, two nodes are extracted and their values compared. 
# Then, the right and left children of the two nodes are inserted in the queue in opposite order. 

# The algorithm is done when either the queue is empty, 
# or we detect that the tree is not symmetric 
# (i.e. we pull out two consecutive nodes from the queue that are unequal).
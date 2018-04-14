# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        stk = []
        intree = []
        outtree = []
        p = root
        
        def preorder(p):
            if p is not None: intree.append(p.val)
            else: 
                intree.append(0) 
                return
                
            preorder(p.left)
            preorder(p.right)
        
        preorder(root)
        #print(intree)
        cur = 0
        while(stk or intree[cur] != 0):
            if intree[cur] != 0:
                stk.append(intree[cur])
            elif intree[cur] == 0:
                outtree.append(stk[-1])
                stk.pop()
            cur = cur + 1
            
        return outtree
                
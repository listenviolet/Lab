# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(stop):
            if preorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
            return None # can be skipped
        
        preorder.reverse()
        inorder.reverse()
        return build(None)

# 这里用到reverse只是为了按原来序列从前到后取值方便，
# 因为可以直接pop出来
# 而无需从前取值，每次还要将数组其余元素依次向前移位

# 重要的是理解 inorder[-1] != stop
# stop是上一层传的root,
# 如果不等，则相当于这些元素都是它的左子树，
# 然后建立左子树
# 然后，inorder.pop，将根节点元素去除，将该节点的父节点的值作为stop传给右子树，
# 建立右子树

# 即根节点将其本身的值作为root.val传给左子树，
# 根节点值在inorder中pop
# 之后将根节点父节点的值作为stop传给右子树
# beats 99.62%
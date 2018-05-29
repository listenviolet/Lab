# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def child(root):  
            if root is None: 
                str.append("#")
                return
            else: str.append(root.val)
            child(root.left)
            child(root.right)
        str = []
        child(root)
        return str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def child():
            val = next(vals)
            if val == "#":
                return None
            root = TreeNode(int(val))
            root.left = child()
            root.right = child()
            return root
        if not data: return None
        vals = iter(data)
        return child()
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Description:
# Serialization is the process of converting a data structure or object 
# into a sequence of bits so that it can be stored in a file or memory buffer, 
# or transmitted across a network connection link 
# to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string 
# and this string can be deserialized to the original tree structure.

# Example: 

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# Clarification: Just the same as how LeetCode OJ serializes a binary tree. 
# You do not necessarily need to follow this format, 
# so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. 
# Your serialize and deserialize algorithms should be stateless.

# Solution:
# Note: 
# 不可以直接定义类成员str,否则，第一次试验后的结果会影响之后的结果
# 可以在类成员函数中定义，如上Str，这样每次调用都会清零更新
# 这里deseialize中使用了iter，可以依次获取data中下一个元素

# Beats: 97.42%
# Runtime: 175ms
# hard
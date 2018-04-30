class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(0,0)  # dummy node
        self.tail = Node(0,0)  # dummy node
        self.tail.prev = self.head  # 将头尾dummy nodes连起来
        self.head.next = self.tail  # o <=> o
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return -1
        
        node = self.hash[key]     # 获取该节点
        self._remove_node(node)   # 从当前位置移除该节点
        self._move_to_tail(node)  # 在表尾添加该节点--每次get就是对节点的访问
        
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:                    # 如果已经存在
            self.hash[key].value = value        # update value in hash table
            node = self.hash[key]               # 获取该节点
            self._remove_node(node)             # 将当前节点从链表中移除--先移除后添加
        else:
            if len(self.hash) == self.capacity:         # 达到capacity
                del self.hash[self.head.next.key]       # o <=> * <=> ... <=> o 找到头dummy节点下一个，即为最近最少访问的节点
                self.head.next = self.head.next.next    # 为dummy节点连next
                self.head.next.prev = self.head         # 为被删去的*之后的节点连prev
                
            node = Node(key, value)             # 新节点
            self.hash[key] = node               # 添加到hash表中
        self._move_to_tail(node)                # 将节点添加到链表尾
        
    def _move_to_tail(self, node):     # <=> A <=> * <=> O
        node.prev = self.tail.prev     # 添加的新节点node prev与尾节点的前一个节点相连 - * node prev
        self.tail.prev = node          # 添加的新节点node 与尾节点相连 - O tail.prev
        node.prev.next = node          # 原尾节点的前一个与 node相连 -  ：- A.next
        node.next = self.tail          # 添加的新节点node next与尾节点相连 - * node next
        
    def _remove_node(self, node):      # <=> A <=> * <=> O 删去*
        node.prev.next = node.next     # A.next -> O
        node.next.prev = node.prev     # O.prev -> A


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Question:
# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key 
#            if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. 
#                   When the cache reached its capacity, 
#                   it should invalidate the least recently used item 
#                   before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# Solution:
# 首先明确最少使用缓存是指我们要缓存最近使用的数据，
# 如果一个数据长时间没有使用，且又有新的数据加入，
# 那么应该将最长时间没有使用的数据去除。
#

# 使用双向链表记录节点使用情况：
#
# 可以通过一个双向链表完成这样的数据结构，
# 表头表尾均有dummy node
# 表尾表示最近使用过的数据，越接近表头表示越久没有使用过。
#

# hash表键值对记录当前存在于链表中的(key,value):
#
# 由于链表的查找操作速度较慢，为了提高查找的速度，可以通过一个键值对的字典来记录数据。
# 查找时先判断是否在字典中，如果在则需要更新节点的使用情况并返回结果，如果不在则直接返回-1。
# 这样插入数据时也可以通过字典来判断是首次插入还是数据的更新。
#

# 插入操作put: 
#
# 1. 节点已存在：更新链表和hash表
# 2. 节点未存在：分为达到容量和未达容量两种情况插入链表和hash表
#
# 更新节点时，将原来的节点删除，改变节点的内容，再插入到链表尾部。
# 当达到容量时，将链表头部的旧数据节点去除，并在尾部插入新的节点。
# 还没有达到容量上限时，我们只要在尾部直接插入。
#

# Beats: 95.69%
# hard
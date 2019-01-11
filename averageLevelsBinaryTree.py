"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

import random

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trav(self, level, curr_level,  root):
        if root is None:
            return 0
        else:
            if(curr_level>len(level)):
                level.append(root.val)
            else:
                level[curr_level] = level[curr_level]+root.val
            left = self.trav(level, (curr_level+1), root.left)
            right = self.trav(level, (curr_level+1), root.right)

    def avgLevels(self, root):
        level = []
        curr_level = 1
        self.trav(level, curr_level, root)
        print(level)
        print(curr_level)

    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

temp = Solution()
root = TreeNode(1)

for i in range(0, 15):
    node = TreeNode(random.randint(1, 20))
    temp.insert(root, node) 

temp.avgLevels(root)
    

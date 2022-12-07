# coding=utf-8
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.
"""

from pprint import pprint
from copy import deepcopy
from treeNode import create_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val_list = []
        self.get_vals(root, val_list)
        print val_list
        val_list.sort()
        print val_list

    def get_vals(self, root, vals):
        if root:
            vals.append(int(root.val))
            self.get_vals(root.left, vals)
            self.get_vals(root.right, vals)




if __name__ == '__main__':
    s_msg = '[1,null,3,2]'
    s = create_tree(s_msg)
    sol = Solution()
    rtn = sol.getMinimumDifference(s)
    print rtn




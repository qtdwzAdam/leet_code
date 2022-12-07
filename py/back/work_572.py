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
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.check_sub(s, t):
            return True
        if s.left and self.isSubtree(s.left, t):
            return True
        if s.right and self.isSubtree(s.right, t):
            return True
        return False

    def check_sub(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.check_sub(s.left, t.left) and self.check_sub(s.right,
                t.right)



if __name__ == '__main__':
    s_msg = '[3,4,5,1,2, null,null,0]'
    t_msg = '[4,1,2]'
    s = create_tree(s_msg)
    t = create_tree(t_msg)
    sol = Solution()
    rtn = sol.isSubtree(s, t)
    print rtn




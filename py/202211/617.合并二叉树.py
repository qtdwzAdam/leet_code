#
# @lc app=leetcode.cn id=617 lang=python
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        elif root2:
            return root2
        elif root1:
            return root1
        else:
            return None

        
# @lc code=end


def main():
    from treeNode import create_tree, print_tree
    x = Solution().mergeTrees(create_tree('[1,3,2,5]'), create_tree('[2,1,3,null,4,null,7]'))
    print(print_tree(x)=='[3,4,5,5,4,null,7]')
    x = Solution().mergeTrees(create_tree('[1]'), create_tree('[1,2]'))
    print(print_tree(x)=='[2,2]')


if __name__ == '__main__':
    main()
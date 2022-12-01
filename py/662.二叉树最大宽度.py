#
# @lc app=leetcode.cn id=662 lang=python
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_cnt = 0

        
# @lc code=end


def main():
    from treeNode import create_tree
    x = Solution().widthOfBinaryTree(create_tree('[1,3,2,5,3,null,9]'))
    print(x, x==4)
    x = Solution().widthOfBinaryTree(create_tree('[1,3,2,5,null,null,9,6,null,7]'))
    print(x, x==7)
    x = Solution().widthOfBinaryTree(create_tree('[1,3,2,5]'))
    print(x, x==2)


if __name__ == '__main__':
    main()
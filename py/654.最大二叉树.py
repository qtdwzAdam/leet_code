#
# @lc app=leetcode.cn id=654 lang=python
#
# [654] 最大二叉树
#

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_idx, max_cnt = self.getMax(nums)
        root = TreeNode(max_cnt)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root
    
    def getMax(self, nums):
        if not nums:
            return None, None
        max_idx = 0
        max_cnt = nums[0]
        for idx, x in enumerate(nums):
            if max_cnt < x:
                max_cnt = x
                max_idx = idx
        return max_idx, max_cnt

# @lc code=end

def main():
    from treeNode import create_tree, print_tree
    x = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
    print(print_tree(x)=='[6,3,5,null,2,0,null,null,1]')
    x = Solution().constructMaximumBinaryTree([3,2,1])
    print(print_tree(x)=='[3,null,2,null,1]')


if __name__ == '__main__':
    main()
#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        path = []
        self.search(root, path, ans)
        return ans
    
    def search(self, root, path, ans):
        if not root:
            path.append(None)
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            if path:
                ans.append('->'.join(path))
            return
        self.search(root.left, path, ans)
        path.pop()
        self.search(root.right, path, ans)
        path.pop()

# @lc code=end

def main():
    from treeNode import create_tree, print_tree
    x = Solution().binaryTreePaths(create_tree('[1,2,3,null,5]'))
    print(x == ["1->2->5","1->3"], x)
    x = Solution().binaryTreePaths(create_tree('[1]'))
    print(x == ['1'], x)


if __name__ == '__main__':
    main()
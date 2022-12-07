#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp_map = {}
        res = self.dp(root, dp_map)
        # print(dp_map, res)
        return res
    
    def dp(self, root, dp_map):
        if not root:
            return 0
        id_root = id(root)
        # print(id_root, root.val)
        if id_root in dp_map:
            return dp_map[id_root]
        dp_map[id_root] = max(
            self.dp(root.left, dp_map) + self.dp(root.right, dp_map),
            root.val + 
            ((self.dp(root.left.left, dp_map) + self.dp(root.left.right, dp_map)) if root.left else 0) +
            ((self.dp(root.right.left, dp_map) + self.dp(root.right.right, dp_map)) if root.right else 0),
        )
        return dp_map[id_root]
        
# @lc code=end


def main():
    from treeNode import create_tree
    root = create_tree('[3,2,3,null,3,null,1]')
    x = Solution().rob(root)
    print(x == 7)


if __name__ == '__main__':
    main()
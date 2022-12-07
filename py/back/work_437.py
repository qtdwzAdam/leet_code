"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        self.check_sum(root, sum, 0)
        return self.cnt

    def check_sum(self, root, sum, base):
        if not root: return
        new_base = root.val + base
        if new_base == sum:
            self.cnt += 1
        self.check_sum(root.left, sum, 0)
        self.check_sum(root.right, sum, 0)
        self.check_sum(root.left, sum, new_base)
        self.check_sum(root.right, sum, new_base)



if __name__ == '__main__':
    sol = Solution()
    print sol.pathSum([10,5,-3,3,2,None,11,3,-2,None,1], 8)

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
        from collections import deque
        odd = deque()
        even = deque()
        odd.append(root)
        max_cnt = 0
        while len(odd) or len(even):
            max_cnt = max(max_cnt, self.cal_dis(odd))
            while len(odd):
                now = odd.pop()
                if now:
                    even.append(now.left)
                    even.append(now.right)

            max_cnt = max(max_cnt, self.cal_dis(even))
            while len(even):
                now = even.pop()
                if now:
                    odd.append(now.left)
                    odd.append(now.right)
        return max_cnt

    def cal_dis(self, deq):
        left = 0
        right = 0
        total = len(deq)
        for idx in range(total):
            if deq[idx]:
                left = idx
                break
        for idx in range(total-1, -1, -1):
            if deq[idx]:
                right = idx
                break
        print(deq, left, right)
        return right - left + 1


        
# @lc code=end


def main():
    from treeNode import create_tree, print_tree
    tree = create_tree('[1,3,2,5,3,null,9]')
    print_tree(tree)
    x = Solution().widthOfBinaryTree(tree)
    print(x, x==4)
    x = Solution().widthOfBinaryTree(create_tree('[1,3,2,5,null,null,9,6,null,7]'))
    print(x, x==7)
    x = Solution().widthOfBinaryTree(create_tree('[1,3,2,5]'))
    print(x, x==2)


if __name__ == '__main__':
    main()
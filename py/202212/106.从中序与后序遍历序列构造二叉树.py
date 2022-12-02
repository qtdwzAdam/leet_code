#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def loop(st, end):
            if st > end:
                return None
            # if st == end:
            #     return TreeNode(inorder[st])
            root = TreeNode(postorder.pop())
            idx = val_idx[root.val]
            root.right = loop(idx+1, end)
            root.left = loop(st, idx-1)
            return root
        val_idx = {x: idx for idx, x in enumerate(inorder)}
        root = loop(0, len(inorder)-1)
        return root
    

        
# @lc code=end


def main():
    print('start')
    from py.treeNode import print_tree
    x = Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
    print(print_tree(x) == '[3,9,20,null,null,15,7]')
    x = Solution().buildTree([-1],[-1])
    print(print_tree(x) == '[-1]')
    x = Solution().buildTree([1,2,3,4],[2,1,4,3])
    print(print_tree(x) == '[3,1,4,null,2]')



if __name__ == '__main__':
    main()
    print('end')
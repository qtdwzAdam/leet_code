#
# @lc app=leetcode.cn id=779 lang=python
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0
        if k & 1 == 0:
            return 1 - self.kthGrammar(n-1, k//2)
        else:
            return self.kthGrammar(n-1, (k+1)//2)


# @lc code=end


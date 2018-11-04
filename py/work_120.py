# -*- coding: utf-8 -*-
#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work120.py
# Created on    : 2018-06-09 11:08:02
# Last Modified : 2018-06-09 11:14:35
# Description   :
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# https://leetcode.com/problems/triangle/description/
#########################################################################

class Solution(object):
    @staticmethod
    def solve(tri, deep, out):
        if deep < 0:
            return 0
        for idx, x in enumerate(tri[deep]):
            out[idx] = x + min(out[idx], out[idx+1])
        Solution().solve(tri, deep-1, out)
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = triangle[-1]

        Solution().solve(triangle, len(triangle) - 2, res)
        return res[0]

if __name__ == '__main__':
    tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print tri
    s = Solution()
    res = s.minimumTotal(tri)
    print res


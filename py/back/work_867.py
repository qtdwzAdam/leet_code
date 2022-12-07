# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_867.py
# Created on    : 2019-09-05 09:40:16
# Description   :
# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
#
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
#
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
#
# Note:
#
#     1 <= A.length <= 1000
#     1 <= A[0].length <= 1000
#
#########################################################################

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A: return []
        res = [[x] for x in A[0]]
        for x_list in A[1:]:
            for idx, x in enumerate(x_list):
                res[idx].append(x)
        return res

def main():
    a = [[1,2,3],[4,5,6], [1,2,3]]
    print Solution().transpose(a)
    return 0

if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_798_2.py
# Created on    : 2018-07-15 15:29:50
# Last Modified : 2018-07-22 10:36:10
# Description   :
#########################################################################

class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        change = [1] * n
        for i in range(n):
            change[(i-A[i]+1) % n] -= 1
        for i in range(1, n):
            change[i] += change[i-1]
        return change.index(max(change))

if __name__ == '__main__':
    tic = [2,3,1,4,0, 5,6,7]
    res = Solution().bestRotation(tic)
    assert res == 3


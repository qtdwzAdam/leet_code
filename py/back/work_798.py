# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_798.py
# Created on    : 2018-07-15 15:02:29
# Last Modified : 2018-07-15 15:29:39
# Description   :
#########################################################################

class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_idx = 0
        max_val = -1
        len_n = len(A)
        out = []
        res = 0
        for x in range(len_n):
            out = A[x:]
            out.extend(A[:x])
            res = 0
            for idx, val in enumerate(out):
                if val<= idx:
                    res += 1
            if max_val < res:
                max_val = res
                max_idx = x
        return max_idx

if __name__ == '__main__':
    tic = [2,3,1,4,0]
    res = Solution().bestRotation(tic)
    assert res == 3


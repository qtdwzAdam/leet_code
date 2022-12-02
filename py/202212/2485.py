#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Adam
@file  : 2485.py
@time  : 2022/12/01 14:06
@desc  :
"""
#
# @lc app=leetcode.cn id=2485 lang=python
#

# @lc code=start

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        def cal(_n):
            return int(_n * (_n+1) / 2)
        total = cal(n)
        for x in range(1, n+1):
            _sum = cal(x)
            if total - _sum + x == _sum:
                return x
        return -1

# @lc code=end

def main():
    print('start')
    x = Solution().pivotInteger(1)
    print(x, x==1)
    x = Solution().pivotInteger(8)
    print(x, x==6)
    x = Solution().pivotInteger(4)
    print(x, x==-1)




if __name__ == '__main__':
    main()
    print('end')
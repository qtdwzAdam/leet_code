#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Adam
@file  : 2482.py
@time  : 2022/12/02 16:29
@desc  :
"""


class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        if not grid or not grid[0]:
            return grid
        len_rows = len(grid)
        len_cols = len(grid[0])
        rtn = [[0] * len_cols for _ in range(len_rows)]
        for idx in range(len_rows):
            for idy in range(len_cols):
                rtn[-1][idy] += grid[idx][idy]
        for idx in range(len_rows):
            oneRows = sum(grid[idx])
            for idy in range(len_cols):
                rtn[idx][idy] = (oneRows + rtn[-1][idy])*2 - len_rows - len_cols
        return rtn

def main():
    print('start')
    x = Solution().onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])
    print(x, x==[[0,0,4],[0,0,4],[-2,-2,2]])
    x = Solution().onesMinusZeros([[1,1,1],[1,1,1]])
    print(x, x==[[5,5,5],[5,5,5]])


if __name__ == '__main__':
    main()
    print('end')
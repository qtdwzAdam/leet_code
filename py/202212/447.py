#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Adam
@file  : 447.py
@time  : 2022/12/01 14:14
@desc  :
"""

"""
#
# @lc app=leetcode.cn id=2485 lang=python
#
"""

# @lc code=start

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_cnt = len(points)
        if len_cnt < 3:
            return 0
        distance = [[0] * len_cnt for _ in range(len_cnt)]
        for idx, x in enumerate(points):
            for idy, y in enumerate(points):
                if idx == idy:
                    continue
                if not distance[idx][idy]:
                    distance[idx][idy] = (x[0]-y[0])**2 + (x[1]-y[1])**2
                    distance[idy][idx] = distance[idx][idy] 
        
        ans = 0
        for dis_vals in distance:
            back_map = {}
            for x in dis_vals:
                if x:
                    if not back_map.get(x):
                        back_map[x] = 1
                    else:
                        back_map[x] += 1
            for _, cnt in back_map.items():
                if cnt > 1:
                    ans += cnt * (cnt-1)
        return ans


            



# @lc code=end

def main():
    print('start')
    x = Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
    print(x, x==2)
    x = Solution().numberOfBoomerangs([[1,1],[2,2],[3,3]])
    print(x, x==2)
    x = Solution().numberOfBoomerangs([[1,1]])
    print(x, x==0)


if __name__ == '__main__':
    main()
    print('end')
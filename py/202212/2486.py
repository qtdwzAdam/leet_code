#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Adam
@file  : 2486.py
@time  : 2022/12/01 14:28
@desc  :
"""

"""
#
# @lc app=leetcode.cn id=2486 lang=python
#
"""

# @lc code=start
class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t:
            return 0
        if not s:
            return len(t)
        
        from collections import deque
        t_idx = {}
        for idx, x in enumerate(t):
            if t_idx.get(x):
                t_idx[x].append(idx)
            else:
                t_idx[x] = deque()
                t_idx[x].append(idx)

        cur = 0
        for idx, x in enumerate(s):
            if t_idx.get(x)and t_idx[x][0] == cur:
                t_idx[x].popleft()
                cur += 1
        return len(t) - cur
# @lc code=end

def main():
    print('start')
    x = Solution().appendCharacters('coaching', 'coding')
    print(x, x==4)
    x = Solution().appendCharacters('abcde', 'a')
    print(x, x==0)
    x = Solution().appendCharacters('z', 'abcde')
    print(x, x==5)
    import time
    st = time.time()
    print(time.time() - st)
    print(x, x==5)


if __name__ == '__main__':
    main()
    print('end')
# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work406.py
# Created on    : 2018-06-10 10:53:06
# Last Modified : 2018-06-10 11:09:58
# Description   :
#########################################################################

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        x1 = sorted(people, key=lambda _x: _x[1])
        x2 = sorted(people)
        print x1
        print x2


if __name__ == '__main__':
    so = Solution()
    peo = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    exp = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    res = so.reconstructQueue(peo)
    print res
    assert res == exp

    res = so.reconstructQueue(exp)
    print res
    assert res == exp


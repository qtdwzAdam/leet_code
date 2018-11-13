# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : test373.py
# Created on    : 2018-06-09 15:19:23
# Last Modified : 2018-06-09 17:08:12
# Description   :
#########################################################################

import sys
sys.path.append('..')
from work373 import Solution

def base_fun(da1, da2, k):
    print da1
    print da2
    print k
    sol = Solution()
    res = sol.kSmallestPairs(da1, da2, k)
    print res
    return res

def test1():
    n1 = [1,7,11]
    n2 = [2,4,6]
    k = 3
    assert base_fun(n1, n2, k) == [[1,2],[1,4],[1,6]]

def test2():
    n1 = [1,1,2]
    n2 = [1,2,3]
    k = 2
    assert base_fun(n1, n2, k) == [[1,1],[1,1]]


def test4():
    n1 = [1,1,2]
    n2 = [1,2,3]
    k = 10
    assert base_fun(n1, n2, k) == [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]

def test3():
    n1 = [1,2]
    n2 = [3]
    k = 3
    assert base_fun(n1, n2, k) == [[1,3], [2,3]]


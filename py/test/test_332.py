# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : test332.py
# Created on    : 2018-06-09 22:48:50
# Last Modified : 2018-06-09 22:51:59
# Description   :
#########################################################################

import sys
sys.path.append('..')
from work332 import Solution

def base_fun(tic):
    so = Solution()
    res = so.findItinerary(tic)
    print 'res', res
    return res

def test1():
    tic = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    res = base_fun(tic)
    assert res == ["JFK","NRT","JFK","KUL"]

def test2():
    tic = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    res = base_fun(tic)
    assert res == ["JFK", "MUC", "LHR", "SFO", "SJC"]

def test3():
    tic = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    res = base_fun(tic)
    assert res == ["JFK","ATL","JFK","SFO","ATL","SFO"]

# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work332.py
# Created on    : 2018-06-09 20:04:58
# Last Modified : 2018-06-09 22:48:45
# Description   : https://leetcode.com/problems/reconstruct-itinerary/description/
#########################################################################

import json
from pprint import pprint
from heapq import *
from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tr_dict = defaultdict(list)
        for x in tickets:
            tr_dict[x[0]].append(x[1])
        now = 'JFK'
        checked = set([now])
        res = [now]
        h = []
        for x in tr_dict[now]:
            heappush(h, x)
        while h:
            val = heappop(h)
            res.append(val)
            if val not in checked:
                for x in tr_dict[val]:
                    heappush(h, x)
                checked.add(val)
        return res


if __name__ == '__main__':

    so = Solution()
    tic2 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    tic = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tic1 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    res = so.findItinerary(tic)
    print 'res', res
    assert res == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print ''
    print ''

    print tic1
    res1 = so.findItinerary(tic1)
    print 'res', res1
    assert res1 == ["JFK","ATL","JFK","SFO","ATL","SFO"]



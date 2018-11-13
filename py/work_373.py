# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work373.py
# Created on    : 2018-06-09 14:02:43
# Last Modified : 2018-06-09 17:41:10
# Description   :
#########################################################################

from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0:
            return []
        h = [(nums1[0] + nums2[0], 0, 0)]
        checked = set((0,0))
        res = []
        n1len = len(nums1)
        n2len = len(nums2)
        while h and len(res) < k:
            obj = heappop(h)
            print obj[1], obj[2]
            res.append([nums1[obj[1]], nums2[obj[2]]])
            if (obj[1] < n1len - 1 and (obj[1]+1, obj[2]) not in checked):
                heappush(h, (nums1[obj[1]+1] + nums2[obj[2]], obj[1]+1, obj[2]))
                checked.add((obj[1]+1, obj[2]))
            if (obj[2] < n2len - 1 and (obj[1], obj[2]+1) not in checked):
                heappush(h, (nums1[obj[1]] + nums2[obj[2]+1], obj[1], obj[2]+1))
                checked.add((obj[1], obj[2]+1))
        return res


if __name__ == '__main__':
    n1 = [1,7,11]
    n2 = [2,4,6]
    k = 3
    print Solution().kSmallestPairs(n1, n2, k)

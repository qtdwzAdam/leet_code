# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work565.py
# Created on    : 2018-06-09 13:36:14
# Last Modified : 2018-06-09 13:47:00
# Description   :
#########################################################################
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0] * len(nums)
        idx = 0
        while(idx >= 0):
            count = 1
            res[idx] = count
            idx = nums[idx]
            while (res[idx] == 0):
                res[idx] = count + 1
                count += 1
                idx = nums[idx]
            try: idx = res.index(0)
            except: idx = -1
        return max(res)


if __name__ == '__main__':
    nums = [5,4,0,3,1,6,2]
    print Solution().arrayNesting(nums)

# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : lc_491.py
# Created on    : 2019-08-09 15:10:01
# Description   :
#   Given an integer array, your task is to find all the different possible
#   increasing subsequences of the given array, and the length of an increasing
#   subsequence should be at least 2.
# Example
#  Input: [4, 6, 7, 7]
#  Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note
#  The length of the given array will not exceed 15.
#  The range of integer in the given array is [-100,100].
#  The given array may contain duplicates, and two equal integers should also
#    be considered as a special case of increasing sequence.
#########################################################################

def main():
    obj = [4, 6, 7, 7]
    s = Solution()
    res = s.findSubsequences(obj)
    exp = [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
    print res
    return 0

class Solution:
    def findSubsequences(self, nums):
        res = [[nums[0]]]
        idx_map = {nums[0]: -1}
        for i in range(1, len(nums)):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = len(res)
                res += [lst + [nums[i]] for lst in res if lst[-1] <= nums[i]] + [[nums[i]]]
            else:
                tmp = len(res)
                res += [res[j] + [nums[i]] for j in range(tmp) if res[j][-1] <= nums[i] and j >= idx_map[nums[i]]]
                idx_map[nums[i]] = tmp
        return [lst for lst in res if len(lst) > 1]
# class Solution(object):
    # def loopSubInc(self, nums, items, idx):
        # if idx < len(nums):
            # if items[-1] <= nums[idx]:
                # items.append(nums[idx])
                # yield items
                # for _idx in xrange(idx+1, len(nums)):
                    # print items, _idx
                    # for x in self.loopSubInc(nums, items, _idx):
                        # yield x
            # for _idx in xrange(idx+1, len(nums)):
                # print items, _idx
                # for x in self.loopSubInc(nums, [nums[idx]], _idx):
                    # yield x


    # def findSubsequences(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: List[List[int]]
        # """
        # if len(nums) < 2:
            # return []
        # res = set()
        # for idx in xrange(1, len(nums)):
            # for x in self.loopSubInc(nums, [nums[0]], idx):
                # res.add('_'.join(str(_x) for _x in x))
        # return [x.split('_') for x in res]



if __name__ == '__main__':
    main()


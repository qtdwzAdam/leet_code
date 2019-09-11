# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_724.py
# Created on    : 2019-09-11 17:23:03
# Description   :
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
#
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
#
# Example 1:
#
# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
#
#
#
# Example 2:
#
# Input:
# nums = [1, 2, 3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
#
# Note:
#
#     The length of nums will be in the range [0, 10000].
#     Each element nums[i] will be an integer in the range [-1000, 1000].
#########################################################################

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        sum_now = 0
        half_sum = s / 2
        for idx, x in enumerate(nums):
            if sum_now == s - sum_now - nums[idx]:
                return idx
            sum_now += x
        return -1

def main():
    nums = [1, 7, 3, 6, 5, 6]
    nums = [1,2,3]
    print Solution().pivotIndex(nums)
    return 0

if __name__ == '__main__':
    main()


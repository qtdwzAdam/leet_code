# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_645.py
# Created on    : 2019-09-05 16:06:30
# Description   :
# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
# Note:
#
#     The given array size will in the range [2, 10000].
#     The given array's numbers won't have any order.
#########################################################################
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        multi_all = 0
        multi_this = 0
        sum_all = n*(n+1)/2
        sum_this = 0
        for idx, x in enumerate(nums):
            multi_all += (idx+1)*(idx+1)
            multi_this += x*x
            sum_this +=x
        a2_b2 = multi_this - multi_all
        a_b = sum_this - sum_all
        a = (a2_b2/a_b + a_b) / 2
        b = a - a_b
        return [a, b]


def main():
    nums = [x+1 for x in xrange(10000)]
    nums[1999] = 2
    print Solution().findErrorNums(nums)
    return 0

if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_334.py
# Created on    : 2019-09-03 09:12:00
# Description   :
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: true
# Example 2:
#
# Input: [5,4,3,2,1]
# Output: false
#########################################################################

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        less, more = [ 0 for i in xrange(len(nums)) ], [ 0 for i in xrange(len(nums)) ]
        mini = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] > mini:
                less[i] = 1
            else:
                mini = nums[i]
        maxim = nums[-1]
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < maxim:
                more[i] = 1
            else:
                maxim = nums[i]
        print more
        print less
        for i in xrange(len(nums)):
            if less[i] and more[i]:
                return True
        return False


def main():
    nums = [1,0,2,0,5]
    print Solution().increasingTriplet(nums)
    return 0

if __name__ == '__main__':
    main()


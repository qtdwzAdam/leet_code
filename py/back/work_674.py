# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_674.py
# Created on    : 2019-09-05 10:10:05
# Description   :
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
#
# Note: Length of the array will not exceed 10,000.
#
#########################################################################

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        maxCnt = 1
        now = 1
        for idx, x in enumerate(nums[1:]):
            if x > nums[idx]:
                now += 1
            else:
                if now > maxCnt:
                    maxCnt = now
                now = 1
        if now > maxCnt: return now
        return maxCnt

def main():
    nums = [1,3, 5, 7]
    print Solution().findLengthOfLCIS(nums)
    return 0

if __name__ == '__main__':
    main()


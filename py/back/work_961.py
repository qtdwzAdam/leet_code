# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_961.py
# Created on    : 2019-09-05 10:20:40
# Description   :
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.
#
# Example 1:
#
# Input: [1,2,3,3]
# Output: 3
#
# Example 2:
#
# Input: [2,1,2,5,3,2]
# Output: 2
#
# Example 3:
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5

#########################################################################

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return
        size = len(A)
        idx = 0
        while idx+2 < size:
            if A[idx] == A[idx+1] or A[idx] == A[idx+2]:
                return A[idx]
            if A[idx+2] == A[idx+1]:
                return A[idx+1]
            idx += 3
        return A[-1]

def main():
    a = [1,2,3,1]
    print Solution().repeatedNTimes(a)
    return 0

if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_942.py
# Created on    : 2019-09-05 20:02:14
# Description   :
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
#     If S[i] == "I", then A[i] < A[i+1]
#     If S[i] == "D", then A[i] > A[i+1]
#
# Example 1:
#
# Input: "IDID"
# Output: [0,4,1,3,2]
#
# Example 2:
#
# Input: "III"
# Output: [0,1,2,3]
#
# Example 3:
#
# Input: "DDI"
# Output: [3,2,0,1]
#
#
# Note:
#
#     1 <= S.length <= 10000
#     S only contains characters "I" or "D".
#
#########################################################################
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S: return []
        res = []
        left = 0
        right = len(S)
        for x in S:
            if x == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        res.append(left)
        return res

def main():
    print Solution().diStringMatch("IDID")
    print Solution().diStringMatch("I")
    print Solution().diStringMatch("DDI")
    return 0

if __name__ == '__main__':
    main()


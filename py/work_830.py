# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_830.py
# Created on    : 2019-08-30 14:18:51
# Last Modified : 2019-08-30 15:25:44
# Description   :
#
# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.
#
#
#
# Example 1:
#
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:
#
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:
#
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
#
#
# Note:  1 <= S.length <= 1000
#########################################################################

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) == 0: return []

        res = []
        lo = 0
        hi = 0
        key = S[0]
        for x in S[1:]:
            if key == x:
                hi += 1
            else:
                if hi - lo >= 2: res.append([lo, hi])

                hi += 1
                lo = hi
                key = x
        if hi - lo >= 2: res.append([lo, hi])
        return res


def main():
    s = "bbbaaa"
    print Solution().largeGroupPositions(s)
    return 0

if __name__ == '__main__':
    main()


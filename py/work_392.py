# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_392.py
# Created on    : 2019-08-30 11:27:37
# Last Modified : 2019-08-30 14:03:05
# Description   :
#Given a string s and a string t, check if s is subsequence of t.
#
#You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
#A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
#Example 1:
#s = "abc", t = "ahbgdc"
#
#Return true.
#
#Example 2:
#s = "axc", t = "ahbgdc"
#
#Return false.
#
#Follow up:
#If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

#########################################################################
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        for xs in s:
            idxNew = t[idx:].find(xs)
            if idxNew == -1: return False
            idx += idxNew + 1
        return True
            




def main():
    s = "leeeeetcode"
    t = "leeeeeeeeeeeetcodewwwwwwe"
    print Solution().isSubsequence(s, t)
    return 0

if __name__ == '__main__':
    main()












































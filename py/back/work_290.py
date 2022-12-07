# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_290.py
# Created on    : 2019-09-05 09:11:11
# Description   :
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

#########################################################################

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(pattern) != len(str_list): return False
        from collections import defaultdict
        pat_list = defaultdict(list)
        for idx, x in enumerate(pattern):
            pat_list[x].append(idx)

        chked_pat = set()
        for vals in pat_list.values():
            pat = str_list[vals[0]]
            if pat in chked_pat: return False
            chked_pat.add(pat)
            for xidx in vals[1:]:
                if str_list[xidx] != pat:
                    return False
        return True



def main():
    pattern = 'cbba'
    str = "dog cat cat dog"
    print Solution().wordPattern(pattern, str)
    return 0

if __name__ == '__main__':
    main()


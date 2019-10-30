# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_504.py
# Created on    : 2019-08-30 14:03:51
# Last Modified : 2019-08-30 14:18:38
# Description   :
# Share
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].
#########################################################################

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = 7
        if num < 0:
            num = -num
            power = "-"
        elif num == 0: return "0"
        else: power = ""

        res = []
        while num > 0:
            res.append(num % 7)
            num = num / 7
        return power + ''.join(str(x) for x in res[::-1])



def main():
    print Solution().convertToBase7(-7)
    return 0

if __name__ == '__main__':
    main()


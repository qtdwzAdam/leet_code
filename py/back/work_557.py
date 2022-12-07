# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_557.py
# Created on    : 2019-09-05 10:38:00
# Description   :
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
#########################################################################
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        for idx, x in enumerate(s_list):
            s_list[idx] = x[::-1]
        return ' '.join(s_list)

def main():
    s = "Let's take LeetCode contest"
    print Solution().reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"

    return 0

if __name__ == '__main__':
    main()


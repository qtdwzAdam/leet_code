# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : lc_349.py
# Created on    : 2019-08-09 16:33:03
# Description   : get group
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]

# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
#########################################################################

def main():
    return 0
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(x for x in nums1 if x in nums2))


if __name__ == '__main__':
    main()


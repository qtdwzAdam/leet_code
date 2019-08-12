# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : lc_962.py
# Created on    : 2019-08-09 16:41:16
# Description   :
# 给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。
# 找出 A 中的坡的最大宽度，如果不存在，返回 0 。

# 示例 1：
# 输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.

# 示例 2：
# 输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.

# 提示：
    # 2 <= A.length <= 50000
    # 0 <= A[i] <= 50000

#########################################################################

def main():
    a = [9,8,1,0,1,9,4,0,4,1]
    a = [0, 1]
    a = [6,0,8,2,1,5]

    res = Solution().maxWidthRamp(a)
    print res
    return 0


class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        expVal = [(idx, x) for idx, x in enumerate(A)]
        expValSort = sorted(expVal, key=lambda x: x[1])
        sortedVal = [x[0] for x in expValSort]
        maxList = [0] * len(A)
        idx = len(A) - 2
        maxList[idx+1] = sortedVal[idx+1]
        while idx >= 0:
            maxList[idx] = max(maxList[idx+1], sortedVal[idx])
            idx -= 1

        print expVal
        print expValSort
        print sortedVal
        print maxList
        maxWidth = 0
        for idx, x in enumerate(sortedVal[:-1]):
            # print "begin", idx, maxWidth
            # maxWidth = max(maxWidth, max(sortedVal[idx+1:]) - x)
            maxWidth = max(maxWidth, maxList[idx] - x)
            # print idx, maxWidth
        return maxWidth

if __name__ == '__main__':
    main()


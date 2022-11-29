#
# @lc app=leetcode.cn id=991 lang=python
#
# [991] 坏了的计算器
#

# @lc code=start
class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        cnt = 0
        while target > startValue:
            if target & 1 == 1:
                target = (target+1) >> 1
                cnt += 2
            else:
                cnt += 1
                target = target >> 1
        return cnt + startValue - target


# @lc code=end


#
# @lc app=leetcode.cn id=2351 lang=python
#
# [2351] 第一个出现两次的字母
#

# @lc code=start
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = set()
        for _s in s:
            if _s in x:
                return _s
            x.add(_s)
# @lc code=end


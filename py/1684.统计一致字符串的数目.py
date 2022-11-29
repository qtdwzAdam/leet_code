#
# @lc app=leetcode.cn id=1684 lang=python
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allow = set(allowed)
        valids = [x for x in words if not(set(x) - allow)]
        return len(valids)
# @lc code=end


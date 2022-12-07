#
# @lc app=leetcode.cn id=806 lang=python
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        length = 0
        for x_alpf in S:
            if length + widths[x_alpf - 'a'] > 100:
                lines += 1
                length = widths[x_alpf - 'a']
            
        
# @lc code=end


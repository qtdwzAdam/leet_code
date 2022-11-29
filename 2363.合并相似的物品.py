#
# @lc app=leetcode.cn id=2363 lang=python
#
# [2363] 合并相似的物品
#

# @lc code=start
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        rtn = {}
        for val, weight in items1:
            if val in rtn:
                rtn[val] += weight
            else:
                rtn[val] = weight
        for val, weight in items2:
            if val in rtn:
                rtn[val] += weight
            else:
                rtn[val] = weight
        return sorted([[x, y] for x,y in rtn.iteritems()])

# @lc code=end


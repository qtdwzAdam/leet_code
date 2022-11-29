# coding=utf-8
# @lc app=leetcode.cn id=1078 lang=python
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        state = 0
        for word in [x for x in text.split(" ") if x]:
            if state == 2:
                res.append(word)
            if word == first:
                state = 1
            elif word == second and state == 1:
                state = 2
            else:
                state = 0
        return res
        
# @lc code=end

if __name__ == "__main__":
    print Solution().findOcurrences("we will we will rock ", "we", 'will')

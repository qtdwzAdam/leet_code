#
# @lc app=leetcode.cn id=942 lang=python
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        res = [0] * right
        for idx, x in enumerate(S):
            if x == 'I':
                res[idx] = left
                left += 1
            elif x == 'D':
                res[idx] = right
                right -= 1
            else:
                print 'error'
        res.append(left)
        return res

        
# @lc code=end


if __name__ == "__main__":
    print Solution().diStringMatch("IDID")
    print 0,4,1,3,2
    print Solution().diStringMatch("III")
    print 0,1,2,3
     
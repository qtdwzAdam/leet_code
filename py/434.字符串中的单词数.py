#
# @lc app=leetcode.cn id=434 lang=python
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        flag = False
        for x in s:
            if x != ' ':
                flag = True
                continue
            if flag:
                cnt += 1
            flag = False
        if flag: cnt +=1
        return cnt
        
# @lc code=end

if __name__ == "__main__":
    print Solution().countSegments("The one-hour drama series Westworld is a dark odyssey about the dawn of artificial consciousness and the evolution of sin. Set at the intersection of the near future and the reimagined past, it explores a world in which every human appetite, no matter how noble or depraved, can be indulged")

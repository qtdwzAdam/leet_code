#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp_table = [False * (len(s)+1)] * (len(p)+1)
        return self.dp(s, p, dp_table)
    
    def dp(self, s, p, dp_table):
        if not p:
            return not s
        if not s:
            return p[-1] == '*'
        if len(p) >= 2 and p[1] == '*':
            return self.dp(s, p[2:], dp_table) or (self.dp(s[1:], p, dp_table) if (s[0] == p[0] or p[0] == '.') else False)
        else:
            if not s:
                return False
            if s[0] != p[0] and p[0] != '.':
                return False
            return self.dp(s[1:], p[1:], dp_table)

# @lc code=end

def main():
    print(Solution().isMatch('a', '.*..a') == False)
    print("xx")
    print(Solution().isMatch('ab', '.*c') == False)
    print(Solution().isMatch('ab', 'a.*') == True)
    print(Solution().isMatch('ab', '.*') == True)
    print(Solution().isMatch('mississippi', 'mis*is*p*.') == False)
    print(Solution().isMatch('aab', 'c*a*b') == True)
    print(Solution().isMatch('ab', 'k.*') == False)


if __name__ == '__main__':
    main()

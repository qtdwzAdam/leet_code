#
# @lc app=leetcode.cn id=784 lang=python
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        path = ""
        st = 0
        cnt = len(s)
        s = s.lower()
        self.loop(s, st, cnt, path, ans)
        return ans
    
    def loop(self, s, st, cnt, path, ans):
        if st == cnt:
            ans.append(path)
            return
        if s[st] == s[st].upper():
            self.loop(s, st+1, cnt, path+s[st], ans)
        else:
            self.loop(s, st+1, cnt, path+s[st], ans)
            self.loop(s, st+1, cnt, path+s[st].upper(), ans)

# @lc code=end


def main():
    print('start')
    x = Solution().letterCasePermutation('a1b2')
    print(x, x==["a1b2", "a1B2", "A1b2", "A1B2"])
    x = Solution().letterCasePermutation('3z4')
    print(x, x==['3z4', '3Z4'])


if __name__ == '__main__':
    main()
    print('end')
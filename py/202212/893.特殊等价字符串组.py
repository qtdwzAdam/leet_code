#
# @lc app=leetcode.cn id=893 lang=python
#
# [893] 特殊等价字符串组
#

# @lc code=start
class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def loop(st,)
        visited = {x: False for x in words}
        total = 0
# @lc code=end


def main():
    print('start')
    x = Solution().numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"])
    print(x, x==3)
    x = Solution().numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"])
    print(x, x==3)


if __name__ == '__main__':
    main()
    print('end')

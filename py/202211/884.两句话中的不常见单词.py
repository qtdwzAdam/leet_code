# coding=utf-8
# @lc app=leetcode.cn id=884 lang=python
#
# [884] 两句话中的不常见单词
#

# @lc code=start
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        def get_uniq_set(s):
            the_set = set()
            all = set()
            s_list = s.split(" ")
            for x in s_list:
                if x in all:
                    if x in the_set:
                        the_set.remove(x)
                else:
                    the_set.add(x)
                all.add(x)
            return the_set, all
        set_a, all_a = get_uniq_set(A)
        print set_a, all_a
        set_b, all_b = get_uniq_set(B)
        print set_b, all_b
        res = (set_a - all_b) | (set_b - all_a)
        return [x for x in res]

if __name__ == '__main__':
    so = Solution()
    print so.uncommonFromSentences("s z z z s", 's z ejt')
        
# @lc code=end


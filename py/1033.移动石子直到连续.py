#
# @lc app=leetcode.cn id=1033 lang=python
#
# [1033] 移动石子直到连续
#

# @lc code=start
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # if a >= b or b >= c:
            # return [0, 0]
        a, b, c = sorted([a, b, c])
        max_cnt = b - a - 1 + c - b - 1
        min_cnt = 0
        if b - a == 2 or c - b == 2:
            min_cnt = 1
        else:
            if b - a > 1:
                min_cnt += 1
            if c - b > 1:
                min_cnt += 1

        return [min_cnt, max_cnt]
# @lc code=end


def main():
    x = Solution().numMovesStones(3, 5, 1)
    print(x)


if __name__ == '__main__':
    main()
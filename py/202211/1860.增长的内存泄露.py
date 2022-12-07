#
# @lc app=leetcode.cn id=1860 lang=python
#
# [1860] 增长的内存泄露
#

# @lc code=start
class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        idx = 1
        while idx <= memory1 or idx <= memory2:
            while memory1 >= memory2:
                memory1 -= idx
                idx += 1
                # print('d1', idx, memory1, memory2)
            if memory1 < 0:
                break
            while memory1 < memory2:
                memory2 -= idx
                idx += 1
                # print('d2', idx, memory1, memory2)
            if memory2 < 0:
                break
        if memory1 < 0:
            idx -= 1
            memory1 += idx
        if memory2 < 0:
            idx -= 1
            memory2 += idx
        return [idx, memory1, memory2]
# @lc code=end

def main():
    x1 = Solution().memLeak(2,2)
    print(x1, x1== [3,1,0])
    x1 = Solution().memLeak(8, 11)
    print(x1, x1== [6,0,4])
    x1 = Solution().memLeak(681,1)
    print(x1, x1== [37,15,1])


if __name__ == '__main__':
    main()

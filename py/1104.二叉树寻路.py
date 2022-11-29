#
# @lc app=leetcode.cn id=1104 lang=python
#
# [1104] 二叉树寻路
#

# @lc code=start
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label == 1:
            return [1]
        ans = []
        tmp = label
        st = 1
        pow = 0
        while st <= label:
            st = st << 1
            pow += 1
        if pow & 1 == 0:
            tmp = st + (st >> 1) - 1 - tmp
        while tmp >= 1:
            ans.append(tmp)
            tmp = tmp >> 1
        ans = ans[::-1]
        st = 1
        for idx, val in enumerate(ans):
            st = st << 1
            if idx & 1 == 0:
                continue
            ans[idx] = st + (st >> 1) -1 - val
        return ans
# @lc code=end

def main():
    x = Solution().pathInZigZagTree(3)
    print(x, x==[1,3])
    x = Solution().pathInZigZagTree(4)
    print(x, x==[1,3,4])
    x = Solution().pathInZigZagTree(2)
    print(x, x==[1,2])
    x = Solution().pathInZigZagTree(14)
    print(x, x==[1,3,4,14])
    x = Solution().pathInZigZagTree(26)
    print(x, x==[1,2,6,10,26])


if __name__ == '__main__':
    main()

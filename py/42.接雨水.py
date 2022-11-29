#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_cnt = len(height)
        lmax = height[0]
        rmax = height[-1]
        left = 0
        right = len_cnt - 1
        ans = 0
        while left <= right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax < rmax:
                ans += lmax - height[left]
                left += 1
            else:
                ans += rmax - height[right]
                right -= 1
        return ans
# @lc code=end

def main():
    x = Solution().trap([4,2,0,3,2,5])
    print(x)


if __name__ == '__main__':
    main()


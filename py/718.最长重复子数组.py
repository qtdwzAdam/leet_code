#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        ans = 0
        for st1 in range(len1-1, -1, -1):
            for st2 in range(len2-1, -1, -1):
                if nums1[st1] == nums2[st2]:
                    dp[st1][st2] = dp[st1+1][st2+1] + 1
                    ans = max(ans, dp[st1][st2])
                # print(st1, nums1[st1], st2, nums2[st2], ans, dp)
        return ans
# @lc code=end

if __name__ == '__main__':
    x1 = Solution().findLength([1,2,3,2,1], [3,2,1,4,7])
    assert x1 == 3, 'x1'
    x2 = Solution().findLength([0,1,1,1,1], [1,0,1,0,1])
    assert x2==2, 'x2'
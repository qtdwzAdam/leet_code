#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target, nums):
        import bisect
        len_cnt = len(nums)
        pre_sum = [0 for x in range(len_cnt+1)]
        for idx in range(len_cnt-1, -1, -1):
            pre_sum[idx] = nums[idx] + pre_sum[idx+1]
        for idx, x in enumerate(nums):
            if x >= target:
                return 1
            min_left = bisect.bisect_left(pre_sum, target+pre_sum[idx], idx)
            print(idx, x, min_left, min_left-idx+1)


# @lc code=end

if __name__ == '__main__':
    x1 = Solution().minSubArrayLen(7, [2,3,1,2,4,3])
    assert x1==2, 'xx1'

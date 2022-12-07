#
# @lc app=leetcode.cn id=713 lang=python
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0
        multi_st = 0
        multi_end = 0
        multi_ans = 1
        ans = 0
        len_cnt = len(nums)
        while True:
            if multi_end >= len_cnt:
                break
            multi_ans *= nums[multi_end]
            if multi_ans < k:
                ans += multi_end - multi_st + 1
            else:
                while (multi_ans >= k and multi_st < len_cnt):
                    multi_ans = int(multi_ans / nums[multi_st])
                    multi_st += 1
                if (multi_ans < k):
                    ans += multi_end - multi_st + 1
            multi_end += 1

        return ans


# @lc code=end


def main():
    x1 = Solution().numSubarrayProductLessThanK([1,1,1], 1)
    print(x1)
    assert x1 == 8, 'invalid'


if __name__ == '__main__':
    main()
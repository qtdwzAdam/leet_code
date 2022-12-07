#
# @lc app=leetcode.cn id=813 lang=python
#
# [813] 最大平均值和的分组
#

# @lc code=start
class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        len_cnt = len(nums)
        dp_table = [[0] * (k+1) for _ in range(len_cnt+1)]
        self.dp(nums, 0, 0, k, dp_table)
        return dp_table[0][k]
    
    def dp(self, nums, st, now, k, dp_table):
        if len(nums) - now < k:
            return 0
        if k == 1:
            dp_table[st][k] = 1.0*sum(nums[st:]) / (len(nums)-st)
            return dp_table[st][k]
        if dp_table[st][k]:
            return dp_table[st][k]
        dp_table[st][k] = max(
            1.0* sum(nums[st:now+1]) / (now-st+1) + self.dp(nums, now+1, now+1, k-1, dp_table),
            self.dp(nums, st, now+1, k, dp_table)
        )
        return dp_table[st][k]


# @lc code=end


def main():
    print('start')
    import math
    x = Solution().largestSumOfAverages([9,1,2,3,9], 3)
    print(x, -0.000006 < x-20 < 0.000006)
    x = Solution().largestSumOfAverages([1,2,3,4,5,6,7], 4)
    print(x, -0.000006 < x-20.5 < 0.000006)


if __name__ == '__main__':
    main()
    print('end')
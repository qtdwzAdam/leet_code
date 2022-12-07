#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_cnt = len(nums)
        if len_cnt < 4:
            return max(nums)
        dp_table = [-1] * len_cnt
        x1 = self.dp(nums, 0, len_cnt-1, dp_table)
        print(dp_table)
        dp_table = [-1] * len_cnt
        x2 = self.dp(nums, 1, len_cnt, dp_table)
        print(dp_table)
        return max(x1, x2)
    
    def dp(self, nums, start, end, dp_table):
        if (start >= end):
            return 0
        if dp_table[start] != -1:
            return dp_table[start]
        dp_table[start] = max(
            self.dp(nums, start+1, end, dp_table),
            self.dp(nums, start+2, end, dp_table) + nums[start]
        )
        return dp_table[start]

# @lc code=end

def main():
    x = Solution().rob([1])
    print(x == 1)
    return
    x = Solution().rob([2,3,2])
    print(x == 3)
    x = Solution().rob([1,2,3])
    print(x == 3)


if __name__ == '__main__':
    main()

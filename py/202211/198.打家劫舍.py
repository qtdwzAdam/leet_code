#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_cnt = len(nums)
        dp_table = [-1] * len_cnt
        self.dp(nums, 0, dp_table)
        # print(dp_table)
        return dp_table[0]
    
    def dp(self, nums, start, dp_table):
        if (start >= len(nums)):
            return 0
        if dp_table[start] != -1:
            return dp_table[start]
        dp_table[start] = max(
            self.dp(nums, start+1, dp_table),
            self.dp(nums, start+2, dp_table) + nums[start]
        )
        return dp_table[start]

# @lc code=end

def main():
    x = Solution().rob([1,2,3,1])
    print(x == 4)
    x = Solution().rob([2,7,9,3,1])
    print(x == 12)


if __name__ == '__main__':
    main()

#
# @lc app=leetcode.cn id=457 lang=python
#
# [457] 环形数组是否存在循环
#

# @lc code=start
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x1 = 0
        x2 = nums[nums[x1]]
        len_cnt = len(nums)
        while x1 != x2:
            x1 = nums[(x1+nums[x1]) % len_cnt]
            x2 = nums[(x2+nums[x2]) % len_cnt]
            x2 = nums[(x2+nums[x2]) % len_cnt]
        

# @lc code=end


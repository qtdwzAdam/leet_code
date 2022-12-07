#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1: return True
        idx = 0
        # 下面这个数组是核心，每个点能到的最远距离
        target = [x+nums[x] for x in xrange(n)]
        max_reach = nums[idx]
        while max_reach < n-1:
            # 当前点和能到的点中间哪个点到的最远就用那个
            max_next = max(target[idx:max_reach+1])
            if max_next <= max_reach:
                return False
            # max_reach之前的点都算过了，就忽略
            idx = max_reach + 1
            # 下一个最远点和max_reach直接能到多远的没算过
            max_reach = max_next
        return True

# @lc code=end


#
# @lc app=leetcode.cn id=1004 lang=python
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp_table = []
        self.dp(nums, 0, k, dp_table)
    
    def dp(self, nums, idx, k, dp_table):
        
        # left = 0
        # right = 0
        # len_cnt = len(nums)
        # while right < len_cnt:
        #     if nums[right] == 0:
        #         k -= 1
        #     if k <= 0:
        #         break
        #     right += 1
        # print(right, left)
        # max_cnt = right - left + 1
        # right += 1
        # while right < len_cnt:
        #     if nums[right] == 0:
        #         while nums[left] == 1:
        #             left += 1
        #         left += 1
        #     max_cnt = max(max_cnt, right-left+1)
        #     print(right, left, max_cnt)
        #     right += 1
        # return max_cnt
# @lc code=end

def main():
    # x1 = Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
    # print(x1 == 6)
    # x1 = Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
    # print(x1 == 10)
    x1 = Solution().longestOnes([0,0,1,1,1,0,0], 0)
    print(x1 == 3, x1)


if __name__ == '__main__':
    main()

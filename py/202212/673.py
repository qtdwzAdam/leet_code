#
# @lc app=leetcode.cn id=673 lang=python
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_cnt = len(nums)
        dp_table = [1] * len_cnt
        max_cnt = [0] * len_cnt
        for idx in range(len_cnt-1, -1, -1):
            for idy in range(idx+1, len_cnt):
                if nums[idx] < nums[idy]:
                    dp_table[idx] = dp_table[idy] + 1
                if dp_table[idx] == dp_table[idy] + 1:
                    max_cnt[idx] = 0
        
        print(dp_table)
        max_num = max(dp_table)
        return dp_table.count(max_num)
# @lc code=end


def main():
    print('start')
    x = Solution().findNumberOfLIS([1,3,5,4,7])
    print(x, x==2)
    x = Solution().findNumberOfLIS([1,1,1,1,1])
    print(x, x==5)


if __name__ == '__main__':
    main()
    print('end')

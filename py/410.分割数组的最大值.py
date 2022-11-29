#
# @lc app=leetcode.cn id=410 lang=python
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_all = sum(nums)
        dp_table = [[sum_all] * (len(nums)+1)] * (k+1)
        return self.dp(nums, len(nums)-1, k, dp_table, sum_all)

    def dp(self, nums, idx, k, dp_table, sum_all):
        if k > idx:
            return dp_table[idx][k]
        if dp_table[idx][k] < sum_all:
            return dp_table[idx][k]
        if k == 1:
            dp_table[idx][k] = sum(nums[:idx+1])
            return dp_table[idx][k]
        
        

# @lc code=end


def main():
    x = Solution().splitArray([7,2,5,10,8], 2)
    print(x == 18)
    x = Solution().splitArray([1,2,3,4,5], 2)
    print(x == 9)
    x = Solution().splitArray([1,4,4], 2)
    print(x == 4)
    x = Solution().splitArray([1,4,4], 1)
    print(x == 9)


if __name__ == '__main__':
    main()
#
# @lc app=leetcode.cn id=670 lang=python
#
# [670] 最大交换
#

# @lc code=start
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(num))
        len_cnt = len(nums)
        ans = num
        for idx in range(len_cnt):
            for idy in range(idx+1, len_cnt):
                if nums[idx] >= nums[idy]:
                    continue
                nums[idx], nums[idy] = nums[idy], nums[idx]
                ans = max(ans, int(''.join(nums)))
                nums[idx], nums[idy] = nums[idy], nums[idx]
        return ans

# @lc code=end

def main():
    x = Solution().maximumSwap(2736)
    print(x)
    x = Solution().maximumSwap(9872)
    print(x)


if __name__ == '__main__':
    main()

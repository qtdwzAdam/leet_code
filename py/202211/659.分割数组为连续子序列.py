#
# @lc app=leetcode.cn id=659 lang=python
#
# [659] 分割数组为连续子序列
#

# @lc code=start
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_cnt = len(nums)
        cnt = 1
        for idx in range(len_cnt-1):
            if nums[idx] == nums[idx+1]:
                if cnt < 3:
                    print(idx, cnt)
                    return False
                cnt = 1
            else:
                cnt += 1

        return cnt != 1 and cnt != 2


# @lc code=end

def main():
    x = Solution().isPossible([1,2,3,3,4,4,5,5])
    print(x)


if __name__ == '__main__':
    main()

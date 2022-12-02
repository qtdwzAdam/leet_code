#
# @lc app=leetcode.cn id=523 lang=python
#
# [523] 连续的子数组和
#

# @lc code=start
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        back = {0: -1}
        pre_sum = 0
        for idx, x in enumerate(nums):
            pre_sum = (pre_sum+x) % k
            if pre_sum in back:
                if idx - back[pre_sum]>=2:
                    return True
            else:
                back[pre_sum] = idx

        print(back)
        return False
# @lc code=end


def main():
    print('start')
    x = Solution().checkSubarraySum([23,2,6,4,7], 6)
    print(x, x==True)
    x = Solution().checkSubarraySum([23,2,4,6,7], 6)
    print(x, x==True)
    x = Solution().checkSubarraySum([23,2,6,4,7], 13)
    print(x, x==False)
    x = Solution().checkSubarraySum([23,2,4,6,6], 7)
    print(x, x==True)
    x = Solution().checkSubarraySum([7,6], 7)
    print(x, x==False)
    x = Solution().checkSubarraySum([5,0,0,0], 3)
    print(x, x==True)


if __name__ == '__main__':
    main()
    print('end')
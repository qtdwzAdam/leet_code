#
# @lc app=leetcode.cn id=442 lang=python
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_cnt = len(nums)
        for i in range(len_cnt):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1], 

        res = []
        for idx in range(len_cnt):
            if idx +1 != nums[idx]:
                res.append(nums[idx])
        return res 
            
# @lc code=end


def main():
    x = Solution().findDuplicates([4,3,2,7,8,2,3,1])
    print(x)


if __name__ == '__main__':
    main()
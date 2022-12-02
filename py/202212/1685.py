#
# @lc app=leetcode.cn id=1685 lang=python
#
# [1685] 有序数组中差绝对值之和
#

# @lc code=start
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_cnt = len(nums)
        prex = [0] * (len_cnt + 1)
        for idx, x in enumerate(nums):
            prex[idx+1] = prex[idx] + x
        
        ans = []
        for idx, x in enumerate(nums):
            if idx == 0:
                ans.append(prex[-1] - x * len_cnt)
            elif idx == len_cnt-1:
                ans.append(x * len_cnt - prex[-1])
            else:
                ans.append(x*idx - prex[idx] + (prex[-1] - prex[idx+1]) - x*(len_cnt-idx-1))
        return ans
# @lc code=end


def main():
    print('start')
    x = Solution().getSumAbsoluteDifferences([2,3,5])
    print(x, x==[4,3,5])
    x = Solution().getSumAbsoluteDifferences([1,4,6,8,10])
    print(x, x==[24,15,13,15,21])


if __name__ == '__main__':
    main()
    print('end')
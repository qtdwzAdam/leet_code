#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        idx = 0
        cnt = len(nums)
        self.loop(nums, idx, cnt, path, ans)
        return ans
    
    def loop(self, nums, st, cnt, path, ans):
        if st == cnt:
            ans.append(list(path))
            return
        for idx in range(st, cnt):
            nums[st], nums[idx] = nums[idx], nums[st]
            path.append(nums[st])
            self.loop(nums, st+1, cnt, path, ans)
            path.pop()
            nums[st], nums[idx] = nums[idx], nums[st]

        
# @lc code=end


def main():
    x = Solution().permute([1,2,3])
    print(x, x==[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    x = Solution().permute([0,1])
    print(x, x==[[0,1], [1,0]])


if __name__ == '__main__':
    main()
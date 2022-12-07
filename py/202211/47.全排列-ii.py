#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        idx = 0
        cnt = len(nums)
        visited = [False] * cnt
        nums.sort()
        self.loop(nums, idx, cnt, visited, path, ans)
        return ans
    
    def loop(self, nums, st, cnt, visited, path, ans):
        if st == cnt:
            ans.append(list(path))
            return
        for idx in range(st, cnt):
            if visited[idx] or (idx > 0 and nums[idx] == nums[idx-1] and not visited[idx-1]):
                continue
            nums[st], nums[idx] = nums[idx], nums[st]
            visited[st] = True
            path.append(nums[st])
            self.loop(nums, st+1, cnt, visited, path, ans)
            visited[st] = False
            path.pop()
            nums[st], nums[idx] = nums[idx], nums[st]

# @lc code=end


def main():
    print("start")
    x = Solution().permuteUnique([1,2,1])
    print(x, x==[[1,1,2], [1,2,1], [2,1,1]])
    x = Solution().permuteUnique([0,1])
    print(x, x==[[0,1], [1,0]])
    x = Solution().permuteUnique([1,2,3])
    print(x, x==[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    x = Solution().permuteUnique([0,1,0,0,9])
    print(x, len(x), len([[0,0,0,1,9],[0,0,0,9,1],[0,0,1,0,9],[0,0,1,9,0],[0,0,9,0,1],[0,0,9,1,0],[0,1,0,0,9],[0,1,0,9,0],[0,1,9,0,0],[0,9,0,0,1],[0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],[1,0,9,0,0],[1,9,0,0,0],[9,0,0,0,1],[9,0,0,1,0],[9,0,1,0,0],[9,1,0,0,0]]))


if __name__ == '__main__':
    main()
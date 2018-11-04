class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        set_check = set(nums)
        if k == 0:
            return len(set(x for x in nums if nums.count(x) > 1))
        cnt = 0
        set_used = set()
        for x in set_check:
            if x-k in set_check and (x, x-k) not in set_used:
                cnt += 1
                set_used.add((x, x-k))

            if k+x in set_check and (x+k, x) not in set_used:
                cnt += 1
                set_used.add((x+k, x))
        return cnt

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 1]
    k = 0
    print sol.findPairs(nums, k)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        res = Counter(nums)
        return [x[0] for x in res.most_common(k)]

if __name__ == '__main__':
    sol = Solution()
    print sol.topKFrequent([11,2,3,4,1,2,3,4,2,2,2,1], 2)
        

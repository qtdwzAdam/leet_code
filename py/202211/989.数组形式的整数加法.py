#

# @lc code=start
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        a = int(''.join(str(x) for x in A))
        return [x for x in str(a + K)]
        
# @lc code=end

if __name__ == "__main__":
    print Solution().addToArrayForm([1,2,3,3], 23)
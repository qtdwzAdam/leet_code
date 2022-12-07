
# @lc code=start
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        return len([x for x in words if x in S])
        
# @lc code=end


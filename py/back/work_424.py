"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
from collections import Counter
class AlpCon(object):
    def __init__(self, k):
        self.max_k = k
        self.alp_con = Counter({})
        self.max_lap = ('', 0)
        self.sum_max = 0
        self.sum_all = 0

    def add_one(self, val):
        self.alp_con.update(val)
        if self.alp_con[val] > self.max_lap[1]:
            self.max_lap = (val, self.alp_con[val])
        self.sum_all += 1
        print self.sum_all

        if self.sum_all - self.max_lap[1] > self.max_k:
            return False
        if self.sum_all > self.sum_max:
            self.sum_max = self.sum_all
        return True

    def del_one(self, val):
        self.alp_con.subtract(val)
        self.sum_all -= 1
        max_lap = self.alp_con.most_common()[0]
        self.max_lap = (max_lap, self.alp_con[max_lap])

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        alp = AlpCon(k)
        idx = 0
        left_idx = 0
        while idx < len(s):
            if not alp.add_one(s[idx]):
                alp.del_one(s[left_idx])
                left_idx += 1
            idx += 1
        return alp.sum_max

if __name__ == '__main__':
    sol = Solution()
    print sol.characterReplacement('AABABBA', 1)

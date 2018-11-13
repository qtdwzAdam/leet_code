# coding=utf-8
"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        max_num = max(nums)
        bin_max = bin(max_num)
        len_max = len(bin_max)
        list_check = []
        base_idx = 0
        for idx in range(3, len_max):
            print bin_max[idx]
            if base_idx:
                tmp_check = [x for x in list_check if bin(x)[2 + idx - base_idx] != bin_max[idx]]
                if len(tmp_check) == 1:
                    return max_num ^ tmp_check[0]
                elif not tmp_check:
                    continue
                list_check = tmp_check
            elif bin_max[idx] == '0':
                if not list_check:
                    list_check = [x for x in nums if len(bin(x)) == len_max - idx + 2]
                    base_idx = idx
                    if len(list_check) == 1:
                        return max_num ^ list_check[0]








if __name__ == '__main__':
    sol = Solution()
    nums = [0, 8]
    print sol.findMaximumXOR(nums)

# coding=utf-8
"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        len_num = 1
        while len_num <= num:
            len_num = len_num << 1
        return (len_num - 1) ^ num



if __name__ == '__main__':
    sol = Solution()
    print sol.findComplement(1)

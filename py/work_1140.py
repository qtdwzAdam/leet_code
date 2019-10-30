# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_1140.py
# Created on    : 2019-08-30 16:20:32
# Last Modified : 2019-08-30 16:30:36
# Description   :
# Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
#
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.
#
#
#
# Example 1:
#
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
#
#
# Constraints:
#
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4
#########################################################################

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        m = 1
        idx = 0
        aget = 0
        bget = 0


def main():
    piles = [2, 7, 9, 4, 4]
    print Solution().stoneGameII(piles)
    return 0

if __name__ == '__main__':
    main()



















































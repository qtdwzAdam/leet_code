"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
"""

# coding=utf-8


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        first_line = board[0]
        idx = 0
        len_line = len(first_line)
        while idx < len_line:
            if first_line[idx] == 'X':
                cnt += 1
                idx += 1
                while idx < len_line and first_line[idx] == 'X':
                    idx += 1
                idx -= 1
            idx += 1

        len_obard = len(board)
        idx_board = 1
        while idx_board < len_obard:
            this_line = board[idx_board]
            idx = 0
            len_line = len(this_line)
            while idx < len_line:
                if this_line[idx] == 'X' and board[idx_board-1][idx] != 'X':
                    cnt += 1
                    idx += 1
                    while idx < len_line and this_line[idx] == 'X':
                        idx += 1
                    idx -= 1
                idx += 1
            idx_board += 1
        return cnt

if __name__ == '__main__':
    sol = Solution()
    print sol.countBattleships(["X..X","...X","...X"])

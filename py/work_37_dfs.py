# coding=utf-8
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

input: ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

"""
from pprint import pprint
from copy import deepcopy




class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self._solve(board, 0)

    def _solve(self, board, pos):
        if pos > 80:
            return True
        idx = pos / 9
        idy = pos % 9

        if board[idx][idy] != '.':
            return self._solve(board, pos + 1)

        for i in range(1, 10):
            if self.check_row(board, idx, str(i)) \
                    and self.check_col(board, idy, str(i)) \
                    and self.check_squ(board, idx, idy, str(i)):
                board[idx] = board[idx][:idy] + str(i) + board[idx][idy+1:]
                if self._solve(board, pos + 1):
                    return True
            board[idx] = board[idx][:idy] + '.' + board[idx][idy+1:]
        return False

    def check_row(self, board, x, val):
        for i in range(9):
            if board[x][i] == val:
                return False
        return True

    def check_col(self, board, y, val):
        return not any((x for x in range(9) if board[x][y] == val))

    def check_squ(self, board, x, y, val):
        idx = x / 3 * 3
        idy = y / 3 * 3
        for ix in range(idx, idx + 3):
            for iy in range(idy, idy + 3):
                if board[ix][iy] == val:
                    return False

        return True



if __name__ == '__main__':
    sol = Solution()
    board = ["53..7....", '6..195...', '.98....6.',
             '8...6...3', '4..8.3..1', '7...2...6',
             '.6....28.', '...419..5', '....8..79']
    board = ["..9748...", "7........", ".2.1.9...",
             "..7...24.", ".64.1.59.", ".98...3..",
             "...8.3.2.", "........6", "...2759.."]
    board = ["...2...63", "3....54.1", "..1..398.",
             ".......9.", "...538...", ".3.......",
             ".263..5..", "5.37....8", "47...1..."]
    board = ["1...7..3.", "83.6.....", "..29..6.8",
             "6....49.7", ".9.....5.", "3.75....4",
             "2.3..91..", ".....2.43", ".4..8...9"]
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    pprint(board)
    sol.solveSudoku(board)
    pprint(board)



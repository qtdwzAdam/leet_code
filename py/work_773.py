# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_773.py
# Created on    : 2018-07-22 10:36:21
# Last Modified : 2018-07-29 10:54:35
# Description   :
#########################################################################

class Solution(object):
    solved = False
    soln = 0

    @staticmethod
    def check(board):
        if board[0] == [1,2,3] and board[1] == [4,5,0]:
            return True
        return False

    @staticmethod
    def sole(board, i, j, n):
        if Solution.solved: return
        if Solution.check(board):
            Solution.solved = True
            Solution.soln = n
        if i == 0:
            board[i][j] = board[1][j]
            board[1][j] = 0
            Solution.sole(board, 1, j, n+1)
        else:
            board[i][j] = board[0][j]
            board[0][j] = 0
            Solution.sole(board, 0, j, n+1)
        if j == 1:
            board[i][j] = board[0][j]
            board[0][j] = 0
            Solution.sole(board, i, 0, n+1)
            Solution.sole(board, i, 2, n+1)
        else:
            Solution.sole(board, i, 1, n+1)



    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in (0, 1):
            for j in (0, 1, 2):
                if board[i][j] == 0:
                    Solution.sole(board, i, j, res)
                    break



if __name__ == '__main__':
    so = Solution()
    board = [[1,2,3], [4,0,5]]
    assert so.slidingPuzzle(board) == 1

    # board = [[1,2,3], [5,4,0]]
    # assert so.slidingPuzzle(board) == -1

    board = [[4,1,2], [5,0,3]]
    assert so.slidingPuzzle(board) == 5

    board = [[3,2,4], [1,5,0]]
    assert so.slidingPuzzle(board) == 14

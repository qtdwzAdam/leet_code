# coding=utf-8
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

input: ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

"""
from pprint import pprint
from copy import deepcopy


class OneCheck(object):
    def __init__(self, x):
        self.hold = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.base = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.num = 9
        self.val = 0
        self.idx = x
        self.idx_in = x / 9
        self.idy_in = x % 9

    def get_one(self):
        if len(self.test_list) == 0:
            return False
        return self.test_list.pop()

    def revert_base(self):
        self.hold = deepcopy(self.base)
        self.test_list = list(self.base)
        self.num = len(self.hold)
        self.val = 0

    def set_ele(self, val):
        change_base = val > 0
        if self.val: return True, 'setted'
        try: val = abs(int(val))
        except: return True, 'not a int'
        if val not in self.hold:
            return True, 'not in hold'
        if change_base:
            self.base.remove(val)
        self.hold.remove(val)
        self.test_list = list(self.hold)
        self.num -= 1
        if self.num == 0:
            return False, 'bad'
        return True, 'good'

    def unset_ele(self, val):
        if self.val > 0:
            return True
        val = abs(val)
        if val in self.hold:
            return False
        self.hold.add(val)
        self.num += 1
        return True

    # set the val real!
    def set_val(self, val):
        try: val = int(val)
        except: return False
        self.num = 9
        self.val = val
        return True

    def unset_val(self, val):
        self.num = len(self.hold)
        self.val = 0

    def __cmp__(self, other):
        return self.num > other.num

    def __str__(self):
        if self.val != 0:
            return str(self.val) + '   '
        return ' '.join([str(x) for x in self.hold]) + ';num:' + str(self.num) + '   '


class Sudoku(object):
    def unset_one(self, x, y, val):
        for i in xrange(9):
            self.board[x * 9 + i].unset_ele(val)
            self.board[i * 9 + y].unset_ele(val)
        base_x = x/3 * 3
        base_y = y/3 * 3
        for idx in xrange(base_x, base_x + 3):
            for idy in xrange(base_y, base_y + 3):
                if not self.board[idx * 9 + idy].unset_ele(val):
                    print 'failed of group of unset'
                    return False
        return True

    def set_one(self, x, y, val):
        for i in xrange(9):
            if not self.board[x * 9 + i].set_ele(val):
                print 'failed of x*9+i'
                return False
            if not self.board[i * 9 + y].set_ele(val):
                print 'failed of i*9+y'
                return False
        base_x = x/3 * 3
        base_y = y/3 * 3
        for idx in xrange(base_x, base_x + 3):
            for idy in xrange(base_y, base_y + 3):
                if not self.board[idx * 9 + idy].set_ele(val):
                    print 'failed of group to set'
                    return False
        return True

    def __init__(self, board):
        self.board = [OneCheck(x) for x in range(81)]
        for idx_line, one_line in enumerate(board):
            for idx_num, one_num in enumerate(one_line):
                if self.board[idx_line*9 + idx_num].set_val(one_num):
                    self.set_one(idx_line, idx_num, int(one_num))

        min_test = min(self.board, key=lambda x: x.num)
        self.steps = []
        while min_test.num < 9:
            if min_test.num == 0:
                last_step = self.steps.pop()
                last_board = self.board[last_step[0]]
                self.unset_one(last_board.idx/9, last_board.idx%9, last_step[1])
                while len(last_board.test_list) == 0:
                    last_board.revert_base()
                    last_step = self.steps.pop()
                    last_board = self.board[last_step[0]]
                    self.unset_one(last_board.idx/9, last_board.idx%9, last_step[1])
            else:
                _this_val = min_test.get_one()
                while _this_val:
                    _val = -1 * _this_val
                    if not self.set_one(min_test.idx/9, min_test.idx%9, _val):
                        self.unset_one(min_test.idx/9, min_test.idx%9, _val)
                        _this_val = min_test.get_one()
                        continue
                    min_test.set_val(_val)
                    self.steps.append((min_test.idx, _val))
                    break
                if not _this_val:
                    last_step = self.steps.pop()
                    last_board = self.board[last_step[0]]
                    self.unset_one(last_board.idx/9, last_board.idx%9, last_step[1])
                    while len(last_board.test_list) == 0:
                        last_board.revert_base()
                        last_step = self.steps.pop()
                        last_board = self.board[last_step[0]]
                        self.unset_one(last_board.idx/9, last_board.idx%9, last_step[1])
            pprint(self.get_output())
            min_test = min(self.board, key=lambda x: x.num)


    def get_output(self):
        out = []
        for idx, one in enumerate(self.board):
            if idx % 9 == 0:
                out.append('')
            out[-1] += str(abs(one.val))
        return out

    def get_print(self):
        out = []
        for idx, one in enumerate(self.board):
            if idx % 9 == 0:
                out.append([])
            out[-1].append(str(one))
        pprint(out)


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.sudoku = Sudoku(board)
        for idx, one_line in enumerate(self.sudoku.get_output()):
            board[idx] = one_line

        
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
    # board = ["1...7..3.", "83.6.....", "..29..6.8",
    #          "6....49.7", ".9.....5.", "3.75....4",
    #          "2.3..91..", ".....2.43", ".4..8...9"]
    pprint(board)
    sol.solveSudoku(board)
    pprint(board)
    


import random
import unittest
from pprint import pprint
from work_37_dfs import Solution

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        board = ["53..7....", '6..195...', '.98....6.',
                 '8...6...3', '4..8.3..1', '7...2...6',
                 '.6....28.', '...419..5', '....8..79']
        res = ['534678912', '672195348', '198342567',
               '859761423', '426853791', '713924856',
               '961537284', '287419635', '345286179']
        sol = Solution()
        sol.solveSudoku(board)
        print board
        print res
        self.assertEqual(board, res, 'test sum fail')

    def test_b(self):
        board = ["..9748...", "7........", ".2.1.9...",
                 "..7...24.", ".64.1.59.", ".98...3..",
                 "...8.3.2.", "........6", "...2759.."]
        res = ["519748632", "783652419", "426139875",
               "357986241", "264317598", "198524367",
               "975863124", "832491756", "641275983"]
        sol = Solution()
        sol.solveSudoku(board)
        print board
        self.assertEqual(board, res, 'test sum fail')

    def test_c(self):
        board = ["...2...63", "3....54.1", "..1..398.",
                 ".......9.", "...538...", ".3.......",
                 ".263..5..", "5.37....8", "47...1..."]
        res = ["854219763", "397865421", "261473985",
               "785126394", "649538172", "132947856",
               "926384517", "513792648", "478651239"]
        sol = Solution()
        sol.solveSudoku(board)
        pprint(board)
        self.assertEqual(board, res, 'test sum fail')

    def test_d(self):
        board = ["1...7..3.", "83.6.....", "..29..6.8",
                 "6....49.7", ".9.....5.", "3.75....4",
                 "2.3..91..", ".....2.43", ".4..8...9"]
        res = ["169875432", "834621795", "572943618",
               "625134987", "498267351", "317598264",
               "283459176", "956712843", "741386529"]
        sol = Solution()
        sol.solveSudoku(board)
        print board
        self.assertEqual(board, res, 'test sum fail')

    def test_e(self):
        board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
        res = ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]

        sol = Solution()
        sol.solveSudoku(board)
        print board
        self.assertEqual(board, res, 'test sum fail')

if __name__ == '__main__':
    unittest.main()
class Solution(object):
    lenx = 0
    leny = 0
    def set_val(self, board, point, val):
        try:
            board[point[0]][point[1]] = val
        except:
            board[point[0]] = board[point[0]][:point[1]] + str(val) + board[point[0]][point[1]+1:]

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board: return board
        Solution.lenx = len(board)
        Solution.leny = len(board[0])
        if board[click[0]][click[1]] == 'M':
            self.set_val(board, click, 'X')
            return board

        self.dfs_check(board, click)
        return board

    def dfs_check(self, board, point):
        if not( 0 <= point[0] < Solution.lenx and 0 <= point[1] < Solution.leny):
            return
        if board[point[0]][point[1]] not in ['M', 'E']:
            return
        around_cnt = self.check_around(board, point)
        if around_cnt != 0:
            self.set_val(board, point, str(around_cnt))
        else:
            self.set_val(board, point, 'B')
            for one_around in self.around_points(point):
                self.dfs_check(board, one_around)

    def check_one(self, board, point):
        if board[point[0]][point[1]] == 'M':
            return 1
        return 0

    def _aroud_points(self, point):
        return [
                [point[0]-1, point[1]-1],
                [point[0]-1, point[1]],
                [point[0]-1, point[1]+1],
                [point[0], point[1]-1],
                [point[0], point[1]+1],
                [point[0]+1, point[1]-1],
                [point[0]+1, point[1]],
                [point[0]+1, point[1]+1],
                ]

    def around_points(self, ori_point):
        for point in self._aroud_points(ori_point):
            if 0 <= point[0] < Solution.lenx and 0 <= point[1] < Solution.leny:
                yield point

    def check_around(self, board, point):
        cnt = 0
        for one_around in self.around_points(point):
            cnt += self.check_one(board, one_around)
        return cnt

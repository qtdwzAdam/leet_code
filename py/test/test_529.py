import sys
sys.path.append('..')
from work_529 import Solution

def base_fun(da1, da2):
    sol = Solution()
    res = sol.updateBoard(da1, da2)
    return res

def test1():
    p1 = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    p2 = [1, 2]
    p3 = [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    res = base_fun(p1, p2)
    msg = '\n%s\n%s\n\n%s' % (str(p1), str(res), str(p3))
    assert res == p3, msg

def test2():
    p1 = [
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'M', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E']]
    p2 = [3, 0]
    p3 = [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']]
    res = base_fun(p1, p2)
    msg = '\n%s\n%s\n\n%s' % (str(p1), str(res), str(p3))
    assert res == p3, msg

def test3():
    p1 = ["EEEEEEEE","EEEEEEEM","EEMEEEEE","MEEEEEEE","EEEEEEEE","EEEEEEEE","EEEEEEEE","EEMMEEEE"]
    p2 = [0, 0]
    p3 = ["BBBBBB1E","B111BB1M","12M1BB11","M211BBBB","11BBBBBB","BBBBBBBB","B1221BBB","B1MM1BBB"]
    res = base_fun(p1, p2)
    msg = '\n%s\n%s\n\n%s' % (str(p1), str(res), str(p3))
    assert res == p3, msg

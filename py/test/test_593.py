import sys
sys.path.append('..')
from work_593 import Solution

def base_fun(da1, da2, da3, da4):
    sol = Solution()
    res = sol.validSquare(da1, da2, da3, da4)
    print res
    return res


def test1():
    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    assert base_fun(p1, p2, p3, p4) == True
    
def test2():
    p1 = [1,0]
    p2 = [0,1]
    p3 = [-1,0]
    p4 = [0,-1]
    assert base_fun(p1, p2, p3, p4) == True

def test3():
    p1 = [0,0]
    p2 = [5,0]
    p3 = [5,4]
    p4 = [0,4]
    assert base_fun(p1, p2, p3, p4) == False

def test4():
    p1 = [1,1]
    p2 = [5,3]
    p3 = [3,5]
    p4 = [7,7]
    assert base_fun(p1, p2, p3, p4) == False

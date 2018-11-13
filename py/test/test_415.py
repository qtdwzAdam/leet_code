import sys
sys.path.append('..')
from work_415 import Solution

def base_fun(da1, da2):
    sol = Solution()
    res = sol.addStrings(da1, da2)
    print res
    return res

def test1():
    p1 = '1'
    p2 = '2'
    assert base_fun(p1, p2) == str(int(p1) + int(p2))

def test2():
    p1 = '12345'
    p2 = '2345666'
    assert base_fun(p1, p2) == str(int(p1) + int(p2))

def test3():
    p1 = '98'
    p2 = '9'
    assert base_fun(p1, p2) == str(int(p1) + int(p2))


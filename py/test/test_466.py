import sys
sys.path.append('..')
from work_466 import Solution

sol = Solution()

def test1():
    s1 = 'acb'
    n1 = 4
    s2 = 'ab'
    n2 = 2
    res = 2

    rtn = sol.getMaxRepetitions(s1, n1, s2, n2)
    assert res == rtn, 'return is :' + str(rtn)

#def test2():
#    s1 = 'acb'
#    n1 = 4
#    s2 = 'ab'
#    n2 = 2
#    res = 2
#
#    rtn = sol.getMaxRepetitions(s1, n1, s2, n2)
#    assert res == rtn, 'return is :' + str(rtn)

#def test3():
#    s1 = 'acb'
#    n1 = 4
#    s2 = 'ab'
#    n2 = 2
#    res = 2
#
#    rtn = sol.getMaxRepetitions(s1, n1, s2, n2)
#    assert res == rtn, 'return is :' + str(rtn)


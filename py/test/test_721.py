import sys
from pprint import pprint
sys.path.append('..')
from work_721 import Solution

def base_fun(in_data, out_data):
    print 'the input is: '
    pprint(in_data)
    print 'expected output is: '
    pprint(out_data)
    sol = Solution()
    res = sol.accountsMerge(in_data)
    for x in res:
        if x not in out_data:
            return False
    for x in out_data:
        if x not in res:
            return False
    return True

def test1():
    accouts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
        "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
            "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    output = [["John", 'john00@mail.com', 'john_newyork@mail.com',
        'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
            "mary@mail.com"]]
    assert base_fun(accouts, output)

def test2():
    accouts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    output = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
    assert base_fun(accouts, output)

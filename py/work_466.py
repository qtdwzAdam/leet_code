class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        """
        ss1 = s1 * n1
        print ss1
        return 1


def test1():
    s1 = 'acb'
    n1 = 4
    s2 = 'ab'
    n2 = 2
    res = 2

    sol = Solution()

    rtn = sol.getMaxRepetitions(s1, n1, s2, n2)
    print 'rtn msg is: ', rtn

if __name__ == '__main__':
    test1()

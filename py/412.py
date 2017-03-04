class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in xrange(n):
            x = i + 1
            if x % 15 == 0:
                res.append('FizzBuzz')
            elif x % 5 == 0:
                res.append('Buzz')
            elif x % 3 == 0:
                res.append('Fizz')
            else:
                res.append(x)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.fizzBuzz(15)

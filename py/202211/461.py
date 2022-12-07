# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# 0<= x, y < 2^31

class Solution_one_line(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

class Solution_best(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = 0, x^y

        while y:
            y &= y - 1
            x += 1
        return x


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = min(x, y), max(x, y)
        res = 0
        while x:
            if x & 1 != y & 1:
                res += 1
            x = x >> 1
            y = y >> 1

        while y:
            y &= y - 1
            res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.hammingDistance(1, 8)

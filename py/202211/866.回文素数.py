#
# @lc app=leetcode.cn id=866 lang=python
#
# [866] 回文素数
#

# @lc code=start
class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverse(x):
            ans = 0
            while x:
                ans = ans*10 + x % 10
                x = x // 10
            return ans
        min_map = {1: 2, 2: 2, 3: 3, 0: 2}
        if n in min_map:
            return min_map[n]
        if n & 1 == 0:
            n = n + 1
        while True:
            if self.isPrime(n) and reverse(n) == n:
                    return n
            n += 2
            if 10**7 < n < 10**8:
                n = 10**8

    def isPrime(self, x):
        if x < 4:
            return True
        if x & 1 == 0:
            return False
        import math
        stop = math.sqrt(x)
        start = 3
        while start <= stop:
            if x % start == 0:
                return False
            start += 2
        return True
# @lc code=end


def main():
    x = Solution().primePalindrome(8)
    print(x, x==11)
    x = Solution().primePalindrome(20)
    print(x, x==101)
    x = Solution().primePalindrome(9989900)
    print(x, x==100030001)


if __name__ == '__main__':
    main()
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = num1[::-1]
        n2 = num2[::-1]
        len1 = len(n1)
        len2 = len(n2)
        if len1 > len2:
            n1, n2 = n2, n1
            len1, len2 = len2, len1
        inc = 0
        res = ''
        for idx in xrange(len1):
            tmp = int(n1[idx]) + int(n2[idx]) + inc
            if tmp > 9:
                tmp -= 10
                inc = 1
            else: inc = 0
            res += str(tmp)
        for idx in xrange(len1, len2):
            tmp = int(n2[idx]) + inc
            if tmp > 9:
                tmp -= 10
                inc = 1
            else: inc = 0
            res += str(tmp)
        if inc:
            res += '1'
        return res[::-1]

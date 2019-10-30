# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : tmp.py
# Created on    : 2019-08-28 09:12:43
# Last Modified : 2019-08-28 09:22:46
# Description   :
#########################################################################


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 0: return []

        rtn = {x: 0 for x in set(A[0])}
        for x in A[0]:
            rtn[x] += 1

        for word in A[1:]:
            print rtn
            for x in rtn.keys():
                if x not in word:
                    rtn.pop(x)
                else:
                    rtn[x] = min(rtn[x], word.count(x))

        res = []
        for x, cnt in rtn.items():
            res.extend([x] * cnt)
        return res



def main():
    A = ["bella","label","roller"]
    print Solution().commonChars(A)
    return 0

if __name__ == '__main__':
    main()


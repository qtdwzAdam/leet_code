# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_937.py
# Created on    : 2019-08-29 11:15:09
# Last Modified : 2019-08-29 11:44:00
# Description   :
# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
#     Each word after the identifier will consist only of lowercase letters, or;
#     Each word after the identifier will consist only of digits.
#     We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
#
#     Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
#
#     Return the final order of the logs.

# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
#########################################################################

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        idigit = []
        for aLog in logs:
            head, msg = aLog.split(" ", 1)
            if msg[0].isdigit():
                idigit.append('%s %s' % (head, msg))
            else:
                letter.append((head, msg))
        letter.sort(key=lambda x: (x[1], x[0]))
        letter2 = [' '.join(x) for x in letter]
        letter2.extend(idigit)
        return letter2



        


def main():
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
    print Solution().reorderLogFiles(logs)
    return 0

if __name__ == '__main__':
    main()


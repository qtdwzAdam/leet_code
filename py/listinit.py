# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : listinit.py
# Created on    : 2019-09-10 11:36:42
# Description   :
#########################################################################

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def init_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    left = head
    for x in arr[1:]:
        right = ListNode(x)
        left.next = right
        left = right
    return head


def main():
    arr = [1,2,3,4, 41]
    a = init_list(arr)
    while a:
        print a, a.val, a.next
        a = a.next
    return 0

if __name__ == '__main__':
    main()


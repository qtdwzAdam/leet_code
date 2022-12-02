#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Adam
@file  : 2487.py
@time  : 2022/12/01 14:41
@desc  :
"""

"""
#
# @lc app=leetcode.cn id=2487 lang=python
#
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        root = ListNode(10**6)
        ans = root
        invalid_tail = self.get_invalid(head)
        if not invalid_tail:
            return head
        while invalid_tail:
            self.del_invalid(root, invalid_tail)
            invalid_tail = self.get_invalid(invalid_tail)
        return ans.next
    
    def del_invalid(self, head, invalid):
        while head and head.next and head.next.val >= invalid.val:
            head = head.next
        head.next = invalid

    def get_invalid(self, head):
        if not head:
            return head
        
        max_cnt = head.val
        while head:
            if max_cnt < head.val:
                return head
            max_cnt = head.val
            head = head.next
        return head


# @lc code=end

def main():
    print('start')
    from py.listinit import init_list, print_list
    x = Solution().removeNodes(init_list([5,2,13,3,8]))
    print(print_list(x) == [13, 8])
    x = Solution().removeNodes(init_list([1,1,1,1,1]))
    print(print_list(x) == [1,1,1,1,1])
    print(print_list(x) == [1,1,1,1,1])


if __name__ == '__main__':
    main()
    print('end')
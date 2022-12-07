# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_234.py
# Created on    : 2019-09-10 11:33:08
# Description   :
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
#
# Example 2:
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#########################################################################

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse slow
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        slow = prev
        fast = head
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
# class ListNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.next = None

def main():
    from listinit import init_list
    arr = [1, 1,2,444, 2,1, 1]
    head = init_list(arr)
    print Solution().isPalindrome(head)
    return 0

if __name__ == '__main__':
    main()


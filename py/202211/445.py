"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        import Queue
        s1 = Queue.LifoQueue()
        s2 = Queue.LifoQueue()
        while l1:
            s1.put(l1.val)
            l1 = l1.next
        while l2:
            s2.put(l2.val)
            l2 = l2.next

        rtn_head = ListNode(0)
        list_tmp = rtn_head
        inc = 0
        while True:
            if s1.isEmpty() and s2.isEmpty():
                if inc == 1:
                    list_tmp.next = ListNode(inc)
                break
            elif s1.isEmpty():
                new_val = s2.get() + inc
            elif s2.isEmpty():
                new_val = s1.get() + inc
            else:
                new_val = s1.get() + s2.get() + inc
            new_ele = ListNode(new_val % 10)
            inc = new_val / 10;
            list_tmp.next = new_ele
            list_tmp = new_ele
        return rtn_head

                


        

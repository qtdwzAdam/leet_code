#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        second = head
        cnt = 0
        while second and cnt < k:
            second = second.next
            cnt += 1
        if cnt < k:
            k = k % cnt
            first = head
            second = head
            cnt = 0
            while second and cnt < k:
                second = second.next
                cnt += 1
        if not second:
            return head
        while second.next:
            first = first.next
            second = second.next
        second.next = head
        head = first.next
        first.next = None
        return head

# @lc code=end

def main():
    from listinit import init_list, print_list
    x = Solution().rotateRight(init_list([1, 2]), 2)
    print(print_list(x) == [1,2])
    x = Solution().rotateRight(init_list([1, 2]), 1)
    print(print_list(x) == [2,1])
    x = Solution().rotateRight(init_list([1,2,3,4,5]), 2)
    print(print_list(x) == [4,5,1,2,3])
    x = Solution().rotateRight(init_list([0,1,2]), 4)
    print(print_list(x) == [2,0,1])


if __name__ == '__main__':
    main()

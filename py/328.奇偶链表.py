#
# @lc app=leetcode.cn id=328 lang=python
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even_root = head.next
        even = head.next
        loop = True
        while loop:
            if not even.next:
                loop = False
            else:
                odd.next = even.next
                odd = odd.next
            if not odd.next:
                loop = False
            else:
                even.next = odd.next
                even = even.next
        odd.next = even_root
        even.next = None
        return head

        
# @lc code=end

def main():
    from listinit import init_list, print_list
    x = Solution().oddEvenList(init_list([2,1,3,5,6,4,7]))
    print(print_list(x) == [2,3,6,7,1,5,4])
    x = Solution().oddEvenList(init_list([1,2,3,4,5]))
    print(print_list(x) == [1,3,5,2,4])


if __name__ == '__main__':
    main()

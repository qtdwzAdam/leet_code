#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sort(head, None)
    
    def sort(self, head, tail):
        if not head or head == tail:
            return head
        if head.next == tail:
            head.next = None
            return head
        
        fast = head
        slow = head
        while fast != tail:
            fast = fast.next
            slow = slow.next
            if fast != tail:
                fast = fast.next

        mid = slow
        return self.merge(self.sort(head, mid), self.sort(mid, fast))
        

    def merge(self, head_a, head_b):
        head = ListNode(0, None)
        root = head
        while head_a and head_b:
            if head_a.val <= head_b.val:
                root.next = head_a
                root = head_a
                head_a = head_a.next
            else:
                root.next = head_b
                root = head_b
                head_b = head_b.next
        if head_a:
            root.next = head_a
        if head_b:
            root.next = head_b
        return head.next

        
# @lc code=end

def main():
    print('start')
    from listinit import init_list, print_list
    x = Solution().sortList(init_list([-1,5,3,4,0]))
    print(print_list(x) == [-1,0,3,4,5])
    x = Solution().sortList(init_list([]))
    print(print_list(x) == [])
    x = Solution().sortList(init_list([4,2,1,3]))
    print(print_list(x) == [1,2,3,4])


if __name__ == '__main__':
    main()

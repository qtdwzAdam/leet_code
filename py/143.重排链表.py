#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        from collections import deque
        q = deque()
        root = head
        while root:
            q.append(root)
            root = root.next
        root = q.popleft()
        while True:
            if len(q) == 0:
                break
            right = q.pop()
            root.next = right
            root = right
            if len(q) == 0:
                break
            left = q.popleft()
            root.next = left
            root = left
        root.next = None
        return head
        
# @lc code=end

def main():
    from listinit import init_list, print_list
    x = Solution().reorderList(init_list([1,2,3,4]))
    print(print_list(x) == [1,4,2,3])
    x = Solution().reorderList(init_list([1,2,3,4,5]))
    print(print_list(x) == [1,5,2,4,3])


if __name__ == '__main__':
    main()

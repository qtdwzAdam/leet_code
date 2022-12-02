#
# @lc app=leetcode.cn id=2181 lang=python
#
# [2181] 合并零之间的节点
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        root = ListNode()
        ans = root
        head = head.next
        total = 0
        while head:
            if head.val == 0:
                if total:
                    root.next = ListNode(total)
                    root = root.next
                    total = 0
            else:
                total += head.val
            head = head.next
        if total:
            root.next = ListNode(total)
        return ans.next

# @lc code=end


def main():
    print('start')
    from py.listinit import init_list, print_list
    x = Solution().mergeNodes(init_list([0,1,0,3,0,2,2,0]))
    print(print_list(x) == [1,3,4])
    x = Solution().mergeNodes(init_list([0,3,1,0,4,5,2,0]))
    print(print_list(x) == [4, 11])


if __name__ == '__main__':
    main()
    print('end')
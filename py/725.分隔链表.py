#
# @lc app=leetcode.cn id=725 lang=python
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ans = []
        cnt = 0
        root = head
        while root:
            cnt += 1
            root = root.next
        each = cnt // k
        first_ex = cnt % k
        if each == 0:
            root = head
            while root:
                ans.append(root)
                root = root.next
            for x in ans:
                x.next = None
            for _ in range(k-cnt):
                ans.append(None)
            return ans

        root = head
        while k > 0:
            k -= 1
            ans.append(root)
            cnt_x = each
            while cnt_x > 1 and root:
                root = root.next
                cnt_x -= 1
            if not root:
                continue
            if first_ex:
                root = root.next
                first_ex -= 1
            if not root or not root.next:
                continue
            tmp = root.next
            root.next = None
            root = tmp
            # root, root.next = root.next, None
        return ans

        
# @lc code=end

def main():
    from listinit import init_list, print_list
    sol = Solution().splitListToParts(init_list([1,2,3]), 5)
    print([print_list(x) for x in sol] == [[1],[2],[3],[],[]])
    sol = Solution().splitListToParts(init_list([1,2,3,4,5,6,7,8,9,10]), 3)
    print([print_list(x) for x in sol] == [[1,2,3,4],[5,6,7],[8,9,10]])


if __name__ == '__main__':
    main()

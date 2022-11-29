# coding=utf-8
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(msg_in, method=int):
    msg = msg_in[1:-1].split(',')
    msg = [method(x.strip()) if x.strip()!="null" else None for x in msg]
    if not len(msg):
        raise Exception('too short')

    root = TreeNode(msg[0])
    dq = deque()
    dq.append(root)
    len_msg = len(msg)
    idx = 1
    while idx < len_msg:
        toadd = dq.popleft()
        left = msg[idx]
        if left:
            left_node = TreeNode(left)
            dq.append(left_node)
            toadd.left = left_node
        idx += 1
        if idx < len_msg:
            right = msg[idx]
            if right:
                right_node = TreeNode(right)
                dq.append(right_node)
                toadd.right = right_node
            idx += 1
    return root

def print_tree(root):
    if not root: return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

if __name__ == '__main__':
    msg_in = "[3,4,5,1,2, null, 2]"

    root = create_tree(msg_in)
    print_tree(root)

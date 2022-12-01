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
    from collections import deque
    q = deque()
    q2 = deque()
    ans = []
    q.append(root)
    level_data = []
    while True:
        while len(q):
            top = q.popleft()
            if not top:
                level_data.append('null')
                continue
            else:
                level_data.append(str(top.val))
            q2.append(top.left)
            q2.append(top.right)
        if level_data:
            ans.append(level_data)
            level_data = []
        while len(q2):
            top = q2.popleft()
            if not top:
                level_data.append('null')
                continue
            else:
                level_data.append(str(top.val))
            q.append(top.left)
            q.append(top.right)
        if level_data:
            ans.append(level_data)
            level_data = []
        if not len(q) and not len(q2):
            break

    ans = ans[:-1]
    last_line = ans[-1]
    for idx, x in enumerate(last_line[::-1]):
        if x != 'null':
            if idx != 0:
                ans[-1] = ans[-1][:-idx]
            break

    rtn = []
    word_len = 6
    word_half = 3
    total = len(ans)
    st = int((2**(total-1) * word_len)/2 - word_half)
    base = '     '
    for idx, level in enumerate(ans):
        gap = base * (2**(total-idx-1))
        gap = gap[:-4]
        print(' '*st, gap.join('%-4s' % str(x) for x in level))
        st -= word_half
        # print(level)
        rtn.extend(level)
    return '[%s]' % (','.join(rtn))


if __name__ == '__main__':
    msg_in = "[2,1,3,5,4,6,7,8,9,10,11,12,null,14,15]"

    root = create_tree(msg_in)
    print(print_tree(root))

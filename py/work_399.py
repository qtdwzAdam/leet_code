# -*- coding: utf-8 -*-

#########################################################################
# Author        : Adam
# Email         : zju_duwangze@163.com
# File Name     : work_399.py
# Created on    : 2018-07-29 15:06:51
# Last Modified : 2018-07-29 16:06:24
# Description   :
#########################################################################


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        import Queue
        check_val = defaultdict(dict)
        visited = set()
        for idx, x in enumerate(equations):
            check_val[x[0]][x[1]] = values[idx]
            check_val[x[1]][x[0]] = 1.0/values[idx]
            check_val[x[1]][x[1]] = 1.0
            check_val[x[0]][x[0]] = 1.0
            check_qu = Queue.Queue()
            if (x[0], x[1]) not in visited:
                check_qu.put((x[0], x[1]))
                visited.add((x[0], x[1]))
                check_qu.put((x[1], x[0]))
                visited.add((x[1], x[0]))
            while not check_qu.empty():
                to_check_key, to_check_val = check_qu.get()
                obj_val = check_val[to_check_val][to_check_key]
                for sub_x, sub_val in check_val[to_check_key].items():
                    if sub_x == to_check_val: continue
                    check_val[sub_x][to_check_val] = 1 / (obj_val * sub_val)
                    check_val[to_check_val][sub_x] = obj_val * sub_val
                    if (sub_x, to_check_val) not in visited:
                        check_qu.put((to_check_val, sub_x))
                        visited.add((to_check_val, sub_x))
                        check_qu.put((sub_x, to_check_val))
                        visited.add((sub_x, to_check_val))
        res = []
        for x in queries:
            res.append(check_val.get(x[0], {}).get(x[1], -1.0))
        return res


if __name__ == '__main__':
    so = Solution()
    equ = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    res = so.calcEquation(equ, values, queries)
    assert res == [6.0, 0.5, -1.0, 1.0, -1.0]


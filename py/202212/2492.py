#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Adam
@file  : 2492.py
@time  : 2022/12/06 16:16
@desc  :
给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道路，道路距离为 distancei 。城市构成的图不一定是连通的。

两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。

城市 1 和城市 n 之间的所有路径的 最小 分数。

注意：

一条路径指的是两个城市之间的道路序列。
一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。
测试数据保证城市 1 和城市n 之间 至少 有一条路径。
"""



class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        road_map = {}
        for idx, x in enumerate(roads):
            if x[0] not in road_map:
                road_map[x[0]] = {}
            if x[1] not in road_map:
                road_map[x[1]] = {}
            road_map[x[0]][x[1]] = x[2]
            road_map[x[1]][x[0]] = x[2]
        visited = [False] * (n+1)
        validset = set()
        from collections import deque
        q = deque()
        q.append(1)
        q.append(n)
        while len(q):
            now = q.pop()
            if visited[now]:
                continue
            visited[now] = True
            for next_point, info in road_map[now].items():
                validset.add(info)
                q.append(next_point)
        return min(validset)


def main():
    print('start')
    x = Solution().minScore(14, [[12,7,2151],[7,2,7116],[11,14,8450],[11,2,9954],[1,11,3307],[10,7,3561],[10,1,4986],[11,7,7674],[14,2,1764],[11,12,6608],[14,7,1070],[9,8,2287],[14,12,6559],[1,2,1450],[2,12,9165]])
    print(x, x==5)
    x = Solution().minScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]])
    print(x, x==5)
    x = Solution().minScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]])
    print(x, x==5)
    x = Solution().minScore(4, [[1,2,2],[1,3,4],[3,4,7]])
    print(x, x==2)


if __name__ == '__main__':
    main()
    print('end')
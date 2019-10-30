#!/usr/bin/env python
# -*- coding: utf-8 -*-

# **********************************************************
# * Author        : Adam
# * Email         : zju_duwangze@163.com
# * Create time   : 2019/9/11 19:21
# * Filename      : work3.py
# * Description   : 
# **********************************************************


import bisect

def fun(a, b, r):
    res = []
    b_passed = 0
    len_b = len(b)
    for x_a in a:
        idx_b_st = bisect.bisect(b[b_passed:], x_a, lo=b_passed)
        if idx_b_st == len_b:
            return res
        idx_b_end = bisect.bisect(b[b_passed:], x_a + r, lo=b_passed)
        for x_b in b[idx_b_st:idx_b_end]:
            res.append([x_a, x_b])
        b_passed = idx_b_st + 1
    return res

def main():
    a = [1,9,10]
    b = [2,4,6]
    r = 1
    # raw = raw_input()
    # msgs = raw.split('=')
    # a = [int(x) for x in msgs[1].split('}')[0][1:].split(',')]
    # b = [int(x) for x in msgs[2].split('}')[0][1:].split(',')]
    # c = int(msgs[3])
    # print a, b, c

    print fun(a, b, r)


if __name__ == "__main__":
    main()

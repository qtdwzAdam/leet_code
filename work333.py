#!/usr/bin/env python
# -*- coding: utf-8 -*-

# **********************************************************
# * Author        : Adam
# * Email         : zju_duwangze@163.com
# * Create time   : 2019/9/11 19:54
# * Filename      : work333.py
# * Description   : 
# **********************************************************


def fun3(a, b):
    backup = {}
    for from_flight, to_flight in b:
        if backup.get(from_flight):
            a[to_flight] = backup[from_flight]
            backup.pop(from_flight)
            continue
        if a.get(to_flight):
            backup[to_flight] = a[to_flight]
        a[to_flight] = a[from_flight]
        a.pop(from_flight)
    msg = ["%s,%s" % (k, v) for k, v in a.items()]
    msg = sorted(msg)
    for x in msg: print x
def main():
    n1 = int(raw_input())
    a = {}
    while n1:
        tmp = raw_input().split(',')
        a['%s,%s' % (tmp[0], tmp[1])] = tmp[2]
        n1 -= 1
    n2 = int(raw_input())
    b = []
    while n2:
        tmp = raw_input().split(',')
        b.append(('%s,%s' % (tmp[0], tmp[1]),
                  '%s,%s' % (tmp[2], tmp[3])))
        n2 -= 1
    fun3(a, b)
if __name__ == "__main__":
    main()

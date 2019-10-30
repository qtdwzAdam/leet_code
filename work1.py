#!/usr/bin/env python
# -*- coding: utf-8 -*-

# **********************************************************
# * Author        : Adam
# * Email         : zju_duwangze@163.com
# * Create time   : 2019/9/11 19:03
# * Filename      : work1.py
# * Description   : 
# **********************************************************

def fun(s):
    def available(_ch):
        return 'a' <= _ch <= 'z' or 'A' <= _ch <= 'Z' or '0' <= _ch <= '9'
    words = []
    len_s = len(s)
    tmp = ""
    for idx, ch in enumerate(s):
        if available(ch):
            tmp += ch
            if len(tmp) > 20:
                words.append(tmp)
                tmp = ''
            continue

        if ch == '-':
            if idx < len_s - 1 and available(s[idx+1]) and tmp:
                tmp += ch
                if len(tmp) > 20:
                    words.append(tmp)
                    tmp = ''
                continue

        if tmp:
            words.append(tmp)
            tmp = ''

    if tmp:
        words.append(tmp)
    return ' '.join(words[::-1])


def main():
    s = 'I am an 20-yeasr 1 out--stanssssssssssssssssssssssssssssssding @ * -s-u-d- de*nt'
    s = raw_input()
    print fun(s)


if __name__ == "__main__":
    main()

from collections import defaultdict
from copy import deepcopy
from pprint import pprint

def get_one_exp(p, q, this_exp_dict, idx, base_prop):
    # this_exp_dict should be empty from beginning
    if p >= 100:
        this_exp_dict[idx] += base_prop
        return
    this_exp_dict[idx] += p * base_prop / 100.0
    get_one_exp(p+q, q, this_exp_dict, idx + 1, (100-p) * base_prop / 100.0)

def add_one(tmp_dict, now_dict):
    # two group to be one
    for idx, one_pro in tmp_dict.items():
        for idx_in, one_pro_in in now_dict.items():
            yield (idx + idx_in, one_pro * one_pro_in)

def merge_data(data_in):
    # finial data merge
    res = 0
    for key, val in data_in.items():
        res += key * val
    return res

def check_exp(p, q, n):
    n_get = 1
    now_dict = defaultdict(float)
    get_one_exp(p, q, now_dict, 1, 1.0)

    tmp_p = p >> 1
    while tmp_p > 1 and n_get < n:
        tmp_dict = defaultdict(float)
        get_one_exp(tmp_p, q, tmp_dict, 1, 1.0)

        result_dict = defaultdict(float)
        for rtn_msg in add_one(tmp_dict, now_dict):
            result_dict[rtn_msg[0]] += rtn_msg[1]

        now_dict = deepcopy(result_dict)
        n_get += 1
        tmp_p = tmp_p >> 1
    if n_get == n:
        return merge_data(result_dict)
    # for the start prop of 1
    assert tmp_p == 1, 'wrong!!!!!!'
    tmp_dict = defaultdict(float)
    get_one_exp(tmp_p, q, tmp_dict, 1, 1.0)
    while n_get < n:
        result_dict = defaultdict(float)
        for rtn_msg in add_one(tmp_dict, now_dict):
            result_dict[rtn_msg[0]] += rtn_msg[1]

        now_dict = deepcopy(result_dict)
        n_get += 1

    return merge_data(result_dict)

if __name__ == '__main__':
    p, q, n = 50, 75, 50
    res = check_exp(p, q, n)
    print res


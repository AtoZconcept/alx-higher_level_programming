#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    dif_set = set()
    for ele in set_1:
        if ele not in set_2:
            dif_set.add(ele)
    for ele in set_2:
        if ele not in set_1:
            dif_set.add(ele)
    return dif_set

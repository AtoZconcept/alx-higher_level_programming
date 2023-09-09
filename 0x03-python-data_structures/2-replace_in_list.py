#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_element = element
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return "{}".format(my_list)

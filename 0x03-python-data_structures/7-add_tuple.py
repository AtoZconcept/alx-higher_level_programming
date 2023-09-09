#!/usr/bin/python

def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    l2 = len(tuple_b)

    if l1 > 1:
        n1, n2, *lest = tuple_a
    if l2 > 1:
        nm1, nm2, *lest = tuple_b
    if l1 == 1:
        n1 = tuple_a[0]
        n2 = 0
    if l2 == 1:
        nm1 = tuple_b[0]
        nm2 = 0
    if l1 == 0:
        n1 = 0
    if l1 == 0:
        n1 = 0
        n2 = 0
    if l2 == 0:
        nm1 = 0
        nm2 = 0
    new = (n1 + nm1, n2 + nm2)
    return new

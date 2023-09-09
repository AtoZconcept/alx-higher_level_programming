#!/usr/bin/python

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 > 1:
        num1, num2, *lest = tuple_a
    if len2 > 1:
        numm1, numm2, *lest = tuple_b
    if len1 == 1:
        num1 = tuple_a[0]
        num2 = 0
    if len2 == 1:
        numm1 = tuple_b[0]
        numm2 = 0
    if len1 == 0:
        num1 = 0
    if len1 == 0:
        num1 = 0
        num2 = 0
    if len2 == 0:
        numm2 = 0
        numm1 = 0
    new = (num1 + numm1, num2 + numm2)
    return new

#!/usr/bin/python3
for a in range(ord('z'), ord('A') -1, -1):
    c = chr(a)
    case = 'lower' if a % 2 == 0 else 'upper'
    print("{}".format(c), end='') if case == 'lower' else print("{}".format(c.upper()), end='')

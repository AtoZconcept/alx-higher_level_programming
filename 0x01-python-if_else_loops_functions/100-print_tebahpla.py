#!/usr/bin/python3
uppercase = False
for i in range(ord('z'), ord('A') -1, -1):
    if uppercase:
        print("{:c}".format(i).upper(), end="")
    else:
        print("{:c}".format(i), end="")
    uppercase = not uppercase

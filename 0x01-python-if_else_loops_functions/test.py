#!/usr/bin/env python3

uppercase = False  # Start with lowercase

for i in range(ord('z'), ord('A') - 1, -1):  # Start from 'z' and end at 'A'
    if uppercase:
        print("{:c}".format(i).upper(), end='')
    else:
        print("{:c}".format(i), end='')

    uppercase = not uppercase  # Toggle between uppercase and lowercase

print()  # Print a newline to end the line

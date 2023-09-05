#!/usr/bin/python3
for letter_ascii in range(ord('a'), ord('z') + 1):
    if chr(letter_ascii) not in 'eq':
        print("{}".format(chr(letter_ascii)), end='')

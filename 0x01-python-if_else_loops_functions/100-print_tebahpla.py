#!/usr/bin/python3

val = 0
b = 90

for num in range(1, 27):
    if num % 2 == 0:
        val = b
    else:
        val = 123 - num

    b -= 1
    print("{}".format(chr(val)), end="")

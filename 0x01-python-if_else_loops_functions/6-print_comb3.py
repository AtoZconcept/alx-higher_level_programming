#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        end = ', ' if b < 9 or a < 8 else ''
        print("{0}{1}".format(a, b), end=end)
print()

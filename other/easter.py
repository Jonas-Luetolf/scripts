#!/bin/python3
import sys

assert len(sys.argv) == 2, "Usage: python easter.py <year>"
assert sys.argv[1].isdigit(), "Year must be a positive integer"

j = int(sys.argv[1])

a = j % 19
b = j % 4
c = j % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7

x = 22 + d + e

if x <= 31:
    m = 3

else:
    m = 4
    x -= 31

print(f"{x}.{m}.{j}")

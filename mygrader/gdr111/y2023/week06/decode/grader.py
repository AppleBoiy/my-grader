#!/usr/bin/env python3

import sys

import decodeV1 as h000

i = 0
j = -1
text = []
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    i += 1
    line = line.strip()
    if i == 1:
        code_table = line
    elif i == 2:
        j = int(line.split()[0])
    elif line:
        text += [line]
        j -= 1
    if j == 0:
        break

try:
    result = h000.decode(code_table, '\n'.join(text))
    print(result)
except NameError:
    ...

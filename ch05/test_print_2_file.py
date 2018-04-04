from __future__ import print_function


with open('/tmp/data.txt', 'w') as f:
    print(1, 2, 'hello, world', sep=", ", file=f)

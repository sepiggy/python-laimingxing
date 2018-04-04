import os
from collections import Counter

c = Counter()

with open(os.path.expanduser('~/.zsh_history')) as f:
    for line in f:
        cmd = line.strip().split(';')[1]
        if cmd:
            c[cmd] += 1

print(c.most_common(10))

import os
import fnmatch

# 搜索 ~/Git/ 目录下的所有 .py 文件

python_files = ['*.py']
matches = []

for root, dirnames, filenames in os.walk(os.path.expanduser("~/Git")):
    for extensions in python_files:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))


for item in matches:
    print(item)

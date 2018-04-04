import os
import fnmatch


# 生成 ~/Downloads/ 目录下所有的 pdf 文件

pdfs = ['*.pdf']
matches = []

for dirpath, dirnames, filenames in os.walk(os.path.expanduser("~/Downloads/")):
    for pat in pdfs:
        for filename in fnmatch.filter(filenames, pat):
            matches.append(os.path.join(dirpath, filename))

print(matches)

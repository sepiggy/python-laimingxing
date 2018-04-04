import os
import fnmatch


def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)

        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)


if __name__ == '__main__':
    files = {name: os.path.getsize(name)
             for name in find_specific_files(os.path.expanduser('~/Downloads/'))}
    result = sorted(files.items(), key=lambda d: d[1], reverse=True)[:10]
    for i, t in enumerate(result, 1):
        print(i, t[0], t[1])

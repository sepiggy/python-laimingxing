import subprocess


def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def main():
    execute_result = execute_cmd('ls -l')
    print(execute_result)


if __name__ == '__main__':
    main()

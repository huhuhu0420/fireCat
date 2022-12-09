import subprocess
import pexpect
from pexpect import popen_spawn
import sys
import time

def follow (thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    child = pexpect.spawnu('ncat 127.0.0.1 1234 -o 1.txt', logfile=sys.stdout)
    test = pexpect.spawnu('python3 test.py')
    with open("testChat.txt", "r") as logfile:
        loglines = follow(logfile)
        for line in loglines:
            child.sendline(line)
            print(line)

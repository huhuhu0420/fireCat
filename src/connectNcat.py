import pexpect
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
    fileName="1.txt"
    child = pexpect.spawnu('ncat 127.0.0.1 1234 -o '+fileName, logfile=sys.stdout)
    test = pexpect.spawnu('python3 txt2json.py '+fileName+' 1.json')
    web = pexpect.spawnu('python3 ./src/app.py')
    with open("./src/testChat.txt", "r") as logfile:
        loglines = follow(logfile)
        for line in loglines:
            child.sendline(line)
            print(line)

        
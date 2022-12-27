import pexpect
import sys
import time
from tinydb import TinyDB, where

def follow (thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def getIp () -> str:
    db = TinyDB('1.json')  # init db
    ip = ""
    try:
        result = db.search(where("ip") != "")
        ip = [r['ip'] for r in result][0]
    except RuntimeError:
        ip =  ""
    except IndexError:
        ip = ""
    return ip

def clearFile (fileName: str) -> None:
    open(fileName, "w").close()

if __name__ == '__main__':
    fileName="1.txt"
    clearFile("chat.txt")
    db = TinyDB('1.json')  # init db
    db.truncate()  # clear db
    
    # get ip
    ip = ""
    while (ip == ""):
        ip = getIp()
    print(ip)
    # ip = "127.0.0.1"

    # connect ncat
    child = pexpect.spawnu('ncat ' + ip + ' 1234 -o '+fileName)
    child.timeout = 3000   # avoid timeout too quick 
    db.insert({"status":"work"})
    # print(child.read())

    # txt to json
    test = pexpect.spawnu('python3 src/txt2json.py '+fileName+' 1.json')
    test.timeout = 3000
    # # print(test.read())

    with open("chat.txt", "r") as logfile:
        loglines = follow(logfile)
        for line in loglines:
            child.sendline(line)
            #print(line)

        
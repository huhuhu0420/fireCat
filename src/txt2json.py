import time
import json
import sys
from tinydb import TinyDB

def follow (thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def getUserCodeList (line: str) -> str:
    userCode = ""
    userCodeList = []
    object = line.split(' ')
    for obj in object:
        if "user" in obj:
            userCodeList.append(obj[5])
    userCode = ' '.join(userCodeList)
    return userCode

def analyze (line: str ,fileName:str) -> None:
    outDict = dict()
    global selfCode
    attribute = str()
    user = str()
    # self message
    if (line[0] != '<'):
        attribute = 'user'
        global selfCode
        user = selfCode
        content = line[:-1]
        outDict['content'] = content
    # announce
    elif (line[1] == 'a'):
        attribute = 'announce'
        if ("is connected" in line):
            outDict["type"] = "newConnected"
        elif ("already connected" in line):
            outDict["type"] = "alreadyConnected"
        elif ("is disconnected" in line):
            outDict["type"] = "disconnected"
        user = getUserCodeList(line)
    # other user message
    elif (line[1] == 'u'):
        user = line[5]
        attribute = 'user'
        content = line[8:-1]
        outDict['content'] = content
    outDict['attribute'] = attribute
    outDict['user'] = user 

    db.insert(outDict)

def clearFile (fileName: str) -> None:
    open(fileName, "w").close()

selfCode = 0
if __name__ == '__main__':
    db = TinyDB('1.json')  # init db

    arg=sys.argv[1:]
    if(len(arg)<2):
        print("error with arg\n")
        sys.exit()

    srcFile=arg[0]
    targetFile=arg[1]
    print(arg)
    clearFile(arg[1])
    first = 1
    with open(srcFile, "r") as logfile:
        titles = logfile.readlines()
        for title in titles:
            if first == 1:  # get self code
                selfCode = getUserCodeList(title)
                first = 0
            print(title)
            analyze(title,targetFile)
        loglines = follow(logfile)
        for line in loglines:
            print(line)
            analyze(line,targetFile)

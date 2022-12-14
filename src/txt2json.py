import time
import sys
from tinydb import TinyDB, where

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
    attribute = str()
    user = str()
    db = TinyDB('1.json')  # init db
    # self message
    if (line[0] != '<'):
        attribute = 'user'
        global selfCode
        user = selfCode
        content = line[:-1]
        outDict['user'] = user 
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
        outDict['user'] = user 
    # other user message
    elif (line[1] == 'u'):
        user = line[5]
        outDict['user'] = user 
        attribute = 'user'
        content = line[8:-1]
        outDict['content'] = content
    outDict['attribute'] = attribute
    db.insert(outDict)

selfCode = '0'
if __name__ == '__main__':
    db = TinyDB('1.json')  # init db
    arg=sys.argv[1:]
    if(len(arg)<2):
        print("error with arg\n")
        sys.exit()

    srcFile=arg[0]
    targetFile=arg[1]
    outDict = dict()
    print(arg)
    first = 1
    with open(srcFile, "r") as logfile:
        titles = logfile.readlines()
        for title in titles:
            if first == 1:  # get self code
                selfCode = getUserCodeList(title)
                outDict["user"] = selfCode
                outDict["content"] = "[WELCOME TO FIRECAT] YOU ARE"
                db.insert(outDict)
                first = 0
            print(title)
            analyze(title,targetFile)
        loglines = follow(logfile)
        for line in loglines:
            if first == 1:  # get self code
                selfCode = getUserCodeList(line)
                outDict["user"] = selfCode
                outDict["content"] = "[WELCOME TO FIRECAT] YOU ARE"
                db.insert(outDict)
                first = 0
            print(line)
            analyze(line,targetFile)

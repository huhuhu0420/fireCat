import subprocess
import pexpect
# result = subprocess.run(['ncat', '127.0.0.1','1234'], stdout=subprocess.PIPE)
web = pexpect.spawnu('python3 ./src/app.py')
while True:
    pass
# print(result)

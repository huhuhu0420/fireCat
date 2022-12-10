import subprocess
result = subprocess.run(['ncat', '127.0.0.1','1234'], stdout=subprocess.PIPE)
print(result)

import subprocess
import sys

arg = sys.argv[1]
print(arg)
val = subprocess.check_call("sh dis.sh '%s'" % arg, shell=True)
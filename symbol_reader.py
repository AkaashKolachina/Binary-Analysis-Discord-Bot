import subprocess
import sys

SYMBOL_FILE = "symbols.txt"
if len(sys.argv) < 3:
    raise Exception("The number of arguments is incorrect")


executable = sys.argv[1]
symbol = sys.argv[2]
has_symbol = False
call = subprocess.check_call("sh dis.sh '%s'" % executable , shell=True)

file = open(SYMBOL_FILE, "r")
for line in file:
    line = line.rstrip("\n")
    if symbol in line:
        print(line)
        has_symbol = True
file.close()

if not has_symbol:
    print ("Sorry that symbol was not in the table")
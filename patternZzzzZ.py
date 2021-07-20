import sys, re
pattern = r"z\w{3}z"
for line in sys.stdin:
    line = line.rstrip()
    if len(line) == 0:
        break
    else:
       if re.search(pattern, line):
           print(line)

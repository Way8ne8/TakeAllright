import sys, re
pattern = r"(.*(cat).*){2,}"
for line in sys.stdin:
    line = line.rstrip()
    if len(line) == 0:
        break
    else:
       if re.match(pattern, line):
           match = re.match(pattern, line)
           print(line)

import sys, re
pattern = r"\b(cat)\b"
for line in sys.stdin:
    line = line.rstrip()
    if len(line) == 0:
        break
    else:
       if re.search(pattern, line):
           #match = re.match(pattern, line)
           print(line)
    # else:
    #     if len(re.findall(pattern, line)) > 0:
    #         print(line)
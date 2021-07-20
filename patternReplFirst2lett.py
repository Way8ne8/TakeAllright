import sys, re
pattern = r"\b(\w)(\w)(\w*)\b"
p1 = r"\2\1\3"
for line in sys.stdin:
    line = line.rstrip()
    if len(line) == 0:
        break
    else:
        print(re.sub(pattern, p1, line))

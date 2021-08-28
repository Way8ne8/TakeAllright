import sys, re
pattern = r"(\w)\1{1,}"
p1 = r"\1"
for line in sys.stdin:
    line = line.rstrip()
    if len(line) == 0:
        break
    else:
        print(re.sub(pattern, p1, line))
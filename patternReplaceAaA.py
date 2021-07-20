import sys, re
pattern = r"\b[aA]{1,}\b"
rep = r"argh"
for line in sys.stdin:
    line = line.rstrip()
    if len(line) == 0:
        break
    else:
        print (re.sub(pattern, rep, line, 1))


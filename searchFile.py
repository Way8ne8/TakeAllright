import os
import re
import os.path
s = []
os.chdir('1')
for cur_dir, dirs, files in os.walk('.'):
    if re.search(r'.py', str(files)):
        #print(cur_dir, dirs, files)
        s.append(cur_dir)
print(s)
for i in s:
    print(i[2:].replace('\\', "/"))



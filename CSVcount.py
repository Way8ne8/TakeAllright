import csv

with open("Crimes.csv", 'r') as f:
    reader = csv.reader(f)
    s = []
    for row in reader:
        s.append(row[5])
#print (s)
a = 0
b = 0
c = str
for i in s:
    if s.count(i) > a:
        a = s.count(i)
        c = i
print(c)

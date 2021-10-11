a = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
move = int(input())
text = input().strip()
res = []
for i in text:
    res.append(a[(a.index(i) + move) % len(a)])
print('Result: ' + '"', end='')
for i in res:
    print(i,end='')
print('"')
n, m = (int(i) for i in input().split())
a = [list(input()) for i in range(n)]

a.insert(0, [0 for i in range(m)])
a.insert(len(a), [0 for i in range(m)])
for i in range(len(a)):
    a[i].insert(0, 0)
    a[i].insert(len(a), 0)

for i in range(1,len(a)):
    for j in range(1, len(a[i])):
        if a[i][j] == '.':
            a[i][j] = 0

for i in range(1, len(a) - 1):
    for j in range(1, len(a[i]) - 1):
        if a[i][j] == '*':
            if a[i - 1][j] != '*':
                a[i - 1][j] += 1
            if a[i - 1][j + 1] != '*':
                a[i - 1][j + 1] += 1
            if a[i - 1][j - 1] != '*':
                a[i - 1][j - 1] += 1

            if a[i + 1][j] != '*':
                a[i + 1][j] += 1
            if a[i + 1][j + 1] != '*':
                a[i + 1][j + 1] += 1
            if a[i + 1][j - 1] != '*':
                a[i + 1][j - 1] += 1

            if a[i][j - 1] != '*':
                a[i][j - 1] += 1
            if a[i][j + 1] != '*':
                a[i][j + 1] += 1

a.pop(0)
a.pop(-1)
for i in range(len(a)):
    a[i].pop(0)
    a[i].pop(-1)
for i in range(n):
    for j in range(m):
        print(a[i][j], end='')
    print()
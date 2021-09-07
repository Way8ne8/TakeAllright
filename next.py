n, m = (int(i) for i in input().split())
a = [input() for j in range(m)]
k = ['0000']
a.insert(0, *k)
a.insert(len(a), *k)
for i in range(len(a)):
    a[i] = '0' + a[i] + '0'
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':

            a[i-1][j]. = '1'
            # a[i-1][j] = int(a[i-1][j]) + 1
            # a[i+1][j] += 1
            # a[i][j-1] += 1
            # a[i][j + 1] += 1
for i in a:
    print(i)
print(a)
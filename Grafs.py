def find_path(graph, end, start, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, end, node, path)
            if newpath:
                return newpath
    return None


n = int(input())
a, b = [], []
d = {}
for i in range(n):
    a, *b = input().replace(":", " ").split()
    d[a] = b
s = []
m = int(input())
c, f = str, str
for j in range(m):
    c, f = input().split()
    if find_path(d, c, f):
        s.append('Yes!!!')
    else:
        s.append('No')
for h in range(len(s)):
    print(s[h])

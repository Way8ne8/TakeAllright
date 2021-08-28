def find_path(graph,  end, start, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    shortest = None

    for node in graph[start]:

        if node not in path:

            newpath = find_path(graph, node, end, path)

            if newpath:

                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest

n = int(input())
a, b = [],[]
d = {}
for i in range(n):
    a, *b = input().replace(":", " ").split()
    d[a] = b
s = []
m = int(input())
c = []
for j in range(m):
    c.append(input())
# print(d)
# print(c)
for k in c[1:]:
    for l in d.keys():
        if find_path(d, l, k):
            #s.append('Yes')
            if l == k:
                pass
            else:
                if k not in s:
                    s.append(k)
                    #print(k)
                break
        # else:
        #     print(l + ' непредок ' + k)

            #s.append('No')
for t in range(len(s)):
    print(s[t])

text = input()
r = len(text)
text += " "
count = 1
res = ''
for i in range(r):
    if text[i+1] == text[i]:
        count += 1
    else:
        if count == 1:
            res += text[i]
        else:
            res += str(count)+text[i]
            count = 1
print(res)
text = input()
count = ''
for i in range(len(text)):
    if text[i].isdigit():
        count += text[i]
    else:
        if text[i].isalpha():
            if i==0:
                print(text[i], end='')
            else:
                if text[i-1].isdigit():
                    print(text[i]*int(count), end='')
                else:
                    print(text[i], end='')
        count = ''

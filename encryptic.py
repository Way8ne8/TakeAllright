import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    #encrypted.decode('utf-8')
with open("passwords.txt", "r") as pwd:

    p = pwd.read().split()
s =[]

for i in range (len(p)):
    try:
        s.append(simplecrypt.decrypt(p[i],encrypted).decode('utf-8'))
        print(s)
    except simplecrypt.DecryptionException:
        print('2222')
    else:
        break


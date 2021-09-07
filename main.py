#! py
stroka=input()
shifr=input()
s=input()
s2=input()
m={}
m1={}
s1=''
s3=''
for i in range(len(stroka)):
    m[str((stroka[i]))]=str(shifr[i])
    m1[(shifr[i])] = stroka[i]
for i in s:
    if i in stroka:
        s1+=str(m[i])
for i in s2:
    if i in shifr:
        s3+=str(m1[i])
print(s1)
print(s3)
str1=input()
str2=input()
m=0
str1=str1.lower()
str2=str2.lower()
for i in range(len(str1)):
    if str1[i]==str2[i]:
        m=0
        continue
    elif str1[i]<str2[i]:
        m=-1
        break
    else:
        m=1
        break

print(m)
        
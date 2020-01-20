s=input()
new=[]
for i in range(len(s)):
    if s[i]=='+':
        continue
    else:
        new.append(s[i])

for i in range(len(new)):
    new[i]=int(new[i])
new.sort()

for i in range(len(new)):
    print(new[i],end='')
    if i!=(len(new)-1):
        print('+',end='')
 
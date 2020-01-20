import sys
count=0
name=input()
s=[name[i] for i in range(len(name)) ]
#print(s) #thik ache sob
for i in range(len(s)):
    if i == len(s):
        sys.exit()
    else:
        p=s[i]
        if p==0:
            continue
#        print(p)
        count+=1
        for j in range(len(s)):
            if s[j]==p:
                s[j]=0
#                print(s)

if count%2==1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
        
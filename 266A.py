import sys
num=int(input())
s=input()
count=0
for i in range(num):
    if i == (num-1):
        print(count)
        sys.exit()
    elif s[i]==s[i+1]:
        count+=1
    else:
        continue

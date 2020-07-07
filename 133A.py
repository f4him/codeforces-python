
a=input()
count=0
lang={'H','Q','9'}
 
for i in range(len(a)):
    if a[i] in lang:
        count=1
    else:
        continue
if count==1:
    print("YES")
else:
    print("NO")

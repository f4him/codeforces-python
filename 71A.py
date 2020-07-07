m=int(input())
for x in range(m):
    s=str(input())
    if len(s)>10:
        size=len(s)
        print(s[0],size-2,s[size-1], sep='')
    else:
        print(s)
import sys
a=input()
c1=0
c2=0
if a[0].isupper():
    for i in range(len(a)):
        if a[i].isupper():
            c1+=1
    if c1==len(a):
        print(a[0:len(a)].lower())
        sys.exit()
    else:
        print(a)
        sys.exit()
    
else:
    for i in range(len(a)):
        if a[i].isupper():
            c1+=1
    if c1==len(a) or c1==(len(a)-1):
        print(a[0].upper(),end='')
        print(a[1:len(a)].lower())
        sys.exit()
    else:
        print(a)
        sys.exit()

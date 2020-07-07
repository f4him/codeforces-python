num,t=input().split()
num=int(num)
t=int(t)
a=input()
m=[a[p] for p in range(len(a))]
new=m.copy()


for i in range(t):
    for j in range(num-1):
        if m[j]=='B' and m[j+1]=='G':
            new[j]='G'
            new[j+1]='B'
        else:
            continue
    m=new.copy()


for h in range(len(new)):
    print(new[h],end='')
g_n=int(input())

a=input().split()
a=[int(a[j]) for j in range(g_n)]

c1=0
c2=0
c3=0
for i in range(g_n):
    if a[i]==1:
        c1+=1
    elif a[i]==2:
        c2+=1
    elif a[i]==3:
        c3+=1
    else: 
        continue

if c1>=4:
    print(g_n-3)
elif c1>=2 and c2>=1:
    print(g_n-2)
elif c1==1 and c3>=1:
    print(g_n-1)
elif c2>=2:
    print(g_n-1)
else:
    print(g_n)
s=int(input())
a=[]
p=0
m=0
for i in range(s):
    a=input().split()
    a=[int(a[j]) for j in range(2)]
    p=p-a[0]+a[1]
    if p>m:
        m=p
print(m)
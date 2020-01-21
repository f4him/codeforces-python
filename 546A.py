a=input().split()
a=[int(a[j]) for j in range(3)]
total=0
for i in range(a[2]):
    total=total+a[0]*(i+1)

if (total-a[1])<0:
    print(0)
else:
    print(total-a[1])

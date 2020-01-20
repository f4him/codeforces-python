n=int(input())
x=0
y=0
z=0
for i in range(n):
    s=input().split()
    p=int(s[0])
    q=int(s[1])
    r=int(s[2])
    
    x+=p
    y+=q
    z+=r

if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
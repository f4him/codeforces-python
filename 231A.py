num=int(input())
sol=0
for i in range(num):
    p,q,r=input().split()
    p,q,r=[int(p),int(q),int(r)]
    if p+q+r>1:
        sol+=1
print(sol)
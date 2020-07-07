t=int(input())

max=0
g1=0
g2=0
new=0
b=0
for m in range(t):
    
    x=input().split()
    x=[int(x[i]) for i in range(len(x))]
    b=x[3]
    x.pop()
    x.sort()
    #print(x)
    if((x[2]*2-x[0]-x[1])>b):
        print("NO")
    else:
        g1=x[2]-x[1]
        g2=x[2]-x[0]
        new=b-(g1+g2)
        if(new%3==0):
            print("YES")
        else:
            print("NO")
x= int(input())
if x%2==0 and x>=1 and x<=100:
    z=x/2
    y=x/2
    if x%2==0 and y%2==0:
        print('YES')
    else:
        y=y-1
        z=z+1
        if x%2==0 and y%2==0 and x>0 and y>0:
            print('YES')
        else:
            print('NO')
else:
    print('NO')
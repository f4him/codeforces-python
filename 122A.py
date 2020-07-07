
import sys
x=input()
num=int(x)
count=0
lucky={'4','7'}
str=[x[i] for i in range(len(x))]
for i in range(len(x)):
    if x[i] in lucky:
        count=0
    else:
        count=1
        break

if count==0:
    print("YES")
    sys.exit()
elif num%4==0 or num%7==0 or num%47==0:
    print("YES")
else:
    print("NO")


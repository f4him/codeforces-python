n=int(input())
a=input().split()
total=0
half=0
my=0
count=0
for i in range(len(a)):
    a[i]=int(a[i])
a.sort(reverse = True)
for i in range(len(a)):
    total+=a[i]
half=total/2
#print("total is", total,"half is", half)
#for i in range(len(a)):
 #   print("coins sorted",a[i])
for i in range(len(a)):
    if(half>=my):
        my=my+a[i]
        count+=1
    else:
            break
print(count)
x=input()
count=0
m=[x[i] for i in range(len(x))]
t=['h','e','l','l','o']
for i in range(len(m)):
    if count==5:
        break
    elif m[i]==t[count]:
       count+=1
       i+=1
    else:
        continue

if count==5:
    print("YES")
else:
    print("NO")
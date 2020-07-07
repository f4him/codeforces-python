n,k=input().split()
n,k=[int(n), int(k)]
count=0
scores=input().split()
for i in range(len(scores)):
    scores[i]=int(scores[i])

for i in range(len(scores)):
    if scores[i]>=scores[k-1] and scores[i]>0:
        count=count+1
print(count)

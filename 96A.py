import sys
seq=input()
count=1
for i in range(len(seq)):
    if i==len(seq)-1:
        if count<7:
            print('NO')
            sys.exit()
    elif seq[i]==seq[i+1]:
        count=count+1
        if count>=7:
            print('YES')
            sys.exit()
    else:
        count=1
        
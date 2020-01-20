s=[input().split() for i in range(5)]

for i in range(5):
    for j in range(5):
        if s[i][j]=='0':
            continue
        else:
            print(abs(2-i)+abs(2-j))
            break

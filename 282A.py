x=int(input())
var=0
for i in range(x):
    op=input()
    if "++" in op:
        var+=1
    else:
        if "--" in op:
            var-=1

print(var)
    
import math
m, n, a = input().split()
m, n, a = [int(m), int(n), int(a)]
p=math.ceil(m/a)
q=math.ceil(n/a)
print(p*q)
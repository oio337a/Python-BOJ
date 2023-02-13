import re

n = int(input())

for _ in range(n):
    s = input()
    m = re.fullmatch('(100+1+|01)+', s)
    if m:
        print("YES")
    else:
        print('NO')

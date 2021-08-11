N = input().split('-')
num = []

for i in N:
    cnt = 0
    N_1 = i.split('+')
    for j in N_1:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

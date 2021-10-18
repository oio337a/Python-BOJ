N = input().split('-')
num = []  # + 저장 될 리스트

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

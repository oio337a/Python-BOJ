N = int(input())

li = []
for i in range(N):
    li.append(int(input()))

li.sort(reverse=True)
for i in range(N):
    li[i] = li[i] * (i + 1)

print(max(li))

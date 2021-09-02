N = int(input())

li = []

while N > 0:
    li.append(N % 2)
    N //= 2
li.reverse()
print(*li, sep='')

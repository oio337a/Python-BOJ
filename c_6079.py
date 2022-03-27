n = int(input())

s = 0
for i in range(n):
    if s >= n:
        print(i-1)
        break
    s += i
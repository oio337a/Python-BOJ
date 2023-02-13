import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = list(map(int, input().split()))

result = 0

temp = []
for i in range(1, n):
    temp.append(li[i]-li[i-1])
temp.sort()

if k == n:
    result = 0
    print(result)
else:
    for i in range(n-k):
        result += temp[i]
    print(result)

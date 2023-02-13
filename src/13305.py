import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))
oil = list(map(int, input().split()))

total = l[0] * oil[0]
mini_oil = oil[0]
dist = 0

for i in range(1, n-1):
    if oil[i] < mini_oil:
        total += mini_oil*dist
        dist = l[i]
        mini_oil = oil[i]
    else:
        dist += l[i]
    if i == n-2:
        total += mini_oil*dist
print(total)

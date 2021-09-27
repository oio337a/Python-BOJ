import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

presum = [li[0]]
for i in range(len(li) - 1):
    presum.append(max(presum[i] + li[i+1], li[i+1]))
print(max(presum))

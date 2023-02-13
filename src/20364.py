import sys
input = sys.stdin.readline

n, q = map(int, input().split())
visited = [0] * (n+1)

for _ in range(q):
    x = int(input())

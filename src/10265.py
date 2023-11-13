#MT

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
visited = [True] + [False] * n

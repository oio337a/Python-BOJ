# https://www.acmicpc.net/problem/15686
# 치킨 배달

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]



# 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

print(board)
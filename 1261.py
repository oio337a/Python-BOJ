import sys
input = sys.stdin.readline

m, n = map(int, input().split())

miro = [list(input().rstrip()) for _ in range(n)]

print(miro)
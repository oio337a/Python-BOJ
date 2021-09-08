import sys

input = sys.stdin.readline

a, b = map(int, input().split())

li_1 = set(list(map(int, input().split())))
li_2 = set(list(map(int, input().split())))

answer = li_1 - li_2

# 정렬을 하기 전 타입 set
# 정렬을 한 후 타입 list
answer = sorted(answer)
print(len(answer))
print(*answer)

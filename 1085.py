# 4개 입력받기
# 최소값 print
# 0,0 ~ a,b 더 가까운 곳 min 값 대입

x, y, a, b = map(int, input().split())

mini = x

if a - x <= mini:
    mini = a - x
if y <= mini:
    mini = y
if b - y <= mini:
    mini = b-y

print(mini)

# 0 <= n <=99

N = int(input())
n = N
cnt = 0
while 1:

    a = N // 10  # a = 10 자리
    b = N % 10  # b = 1의 자리

    c = a+b
    if c // 10 != 0:
        c = c % 10
    d = (b*10) + c
    cnt += 1
    N = d
    if n == d:
        break

print(cnt)

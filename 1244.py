
n = int(input())

li = list(map(int, input().split()))

k = int(input())

SPLITS = 20
for _ in range(k):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(1, (len(li) // b) + 1):
            b *= i
            if li[b - 1] == 1:
                li[b - 1] = 0
            else:
                li[b - 1] = 1
        # 0, 1, 1, 1, 0, 1, 0, 1
    else:
        li[b-1] = 0 if li[b-1] == 1 else 1
        for j in range(1, len(li)//2):
            if b-j-1 < 0 or b+j-1 >= n:
                break
            if li[b-j-1] == li[b+j-1]:
                li[b-j-1] = 0 if li[b-j-1] == 1 else 1
                li[b+j-1] = 0 if li[b+j-1] == 1 else 1
        # [1, 0, 1, 0, 0, 1, 0, 1]
for idx in range(0, len(li), SPLITS):
    print(*li)

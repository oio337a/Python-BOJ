
n = int(input())

li = list(map(int, input().split()))

k = int(input())

for _ in range(k):
    # a = 성별
    # b = 변경할 인덱스 + 1
    a, b = map(int, input().split())
    if a == 1:  # 남성일때
        for i in range(1, (len(li) // b) + 1):
            q = (b * i) - 1
            li[q] = 0 if li[q] == 1 else 1
    else:
        li[b-1] = 0 if li[b-1] == 1 else 1
        left = b - 2
        right = b
        while left >= 0 and right < n and li[left] == li[right]:
            if li[left] == 0:
                li[left], li[right] = 1, 1
            elif li[left] == 1:
                li[left], li[right] = 0, 0
            # ValueError: too many values to unpack
            # li[left], li[right] = 1, 1 if li[left] == 0 else 0, 0
            left -= 1
            right += 1
            if left < 0 or right >= n:
                break
        # 안된다.. 인덱스 에러
        # for j in range(1, len(li)//2):
        #     if b-j-1 < 0 or b+j-1 >= n:
        #         break
        #     if b-j-1 >= 0 b+j-1 < n
        #     if li[b-j-1] == li[b+j-1]:
        #         li[b-j-1] = 0 if li[b-j-1] == 1 else 1
        #         li[b+j-1] = 0 if li[b+j-1] == 1 else 1

cnt = 0
ans = ''
for i in range(n):
    ans += (str(li[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0
if len(ans) != 0:
    print(ans)

# for idx in range(1, len(li), 20):
#     print(*li[idx:idx+20])
'''
생각해 볼것 
0 또는 1 을 변경하는 문제
li[i] = (li[i]+1) % 2
li[i]가 0 이면 1
li[i]가 1 이면 0
으로 변경
'''

# N 을 입력 받는다.
N = int(input())
# 리스트로 저장
li = list(map(int, input().split()))

li.sort()  # 리스트 정렬
i = 0
cnt = 0
while N >= 1:  # 반복 돌면서
    cnt += li[i]*N  # 각 인덱스 값 만큼 N을 곱해서 더한다.
    i += 1
    N -= 1
print(cnt)

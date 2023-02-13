N = int(input())

for i in range(N):
    nums = list(map(int, input().split()))
    av = sum(nums[1:])/nums[0]
    cnt = 0
    for j in nums[1:]:
        if j > av:
            cnt += 1
    rate = cnt/nums[0]*100
    print((f"{rate:.3f}%"))

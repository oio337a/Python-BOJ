li = list(map(str, input().split()))


for j in range(len(li)):
    for i in range(1, len(li)):
        if li[i] < li[i-1]:
            li[i], li[i-1] = li[i-1], li[i]
            print(' '.join(li))

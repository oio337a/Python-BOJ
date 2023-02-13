import sys
input = sys.stdin.readline

n = int(input())
li = set()

for _ in range(n):
    temp = input().split()

    if len(temp) == 1:  # 커멘드만 입력 받았다면
        if temp[0] == 'all':
            li = set([i for i in range(1, 21)])
        else:
            li = set()

    else:
        co, num = temp[0], temp[1]
        num = int(num)

        if co == 'add':
            li.add(num)
        elif co == 'remove':
            li.discard(num)
        elif co == 'check':
            print(1 if num in li else 0)
        elif co == 'toggle':
            if num in li:
                li.discard(num)
            else:
                li.add(num)

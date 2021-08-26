card = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    card[a-1:b] = reversed(card[a-1:b])

for i in card:
    if i == 20:
        print(i)
    else:
        print(i, end=" ")

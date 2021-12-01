import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []

mo_eum = "aeiou"
ja_eum = "bcdfghjklmnpqrstvwxyz"

weight = dict()
for i in range(len(ja_eum)):
    weight[ja_eum[i]] = i

for i in range(n):
    temp = set()
    for char in input().strip():
        temp.add(char)

    num = 0
    for char in temp:
        if char in mo_eum:
            continue
        num += 1 << weight.get(char)
    li.append(num)

current = (1 << 21) - 1
for i in range(m):
    o, x = input().split()
    if o == '1':
        current -= 1 << weight.get(x)
    else:
        current += 1 << weight.get(x)

    num = 0
    for string in li:
        if current & string == string:
            num += 1

    print(num)

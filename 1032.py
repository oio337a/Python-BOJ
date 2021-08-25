n = int(input())
first = list(input())

for _ in range(n-1):
    b = list(input())
    for i in range(len(first)):
        if first[i] != b[i]:
            first[i] = '?'
print(''.join(first))

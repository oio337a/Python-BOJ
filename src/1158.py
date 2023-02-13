n, k = map(int, input().split())

line = [i for i in range(1, n+1)]
yo_list = []

num = 0

for i in range(n):
    num += k-1
    if num >= len(line):
        num = num % len(line)
    yo_list.append(line.pop(num))

# 출력
print('<', end="")
for i in yo_list:
    if i == yo_list[-1]:
        print(i, end="")
        print('>')
    else:
        print(f"{i}, ", end="")

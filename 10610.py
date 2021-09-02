n = list(input())

answer = -1

n.sort(reverse=True)
n = int(''.join(n))
if n % 30 == 0:
    answer = n
print(answer)

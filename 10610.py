n = list(input())
# 102 [1 0 2]
answer = -1

n.sort(reverse=True) # 가장큰수를 구하여라
# [2 1 0]
n = int(''.join(n))
if n % 30 == 0:
    answer = n
print(answer)

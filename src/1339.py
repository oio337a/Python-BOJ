# 단어 수학

import sys
input = sys.stdin.readline

n = int(input())
alpha_dic = {chr(ord('A') + i): 0 for i in range(26)}
alpha_list = []
answer = 0
pocket = []

for _ in range(n):
    alpha = input().rstrip()
    pocket.append(alpha)

for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet) - i - 1)
        alpha_dic[alphabet[i]] += num

for value in alpha_dic.values():
    if value > 0:
        alpha_list.append(value)

sorted_list = sorted(alpha_list, reverse=True)
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)
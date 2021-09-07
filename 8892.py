from itertools import permutations

n = int(input())
answer = []

for i in range(n):
    a = int(input())
    palin = []
    for j in range(a):
        palin.append(input())
        PLAG = True
    word = list(permutations(palin, 2))
    c = []
    r = []
    for i in word:
        b = ''.join(i)
        c.append(b)
        r.append(b[::-1])
    for i in range(len(c)):
        if c[i] == r[i]:
            answer.append(c[i])
            PLAG = False
            break

    # reverse = [i for i in word[::-1]]
    # for i in range(len(word)):
    #     if word[i] == reverse[i]:
    #         answer.append(word)
    #         PLAG = False
    #         break

    # for k in range(0, a):
    #     for q in range(0, a):
    #         if k == q:
    #             continue
    #         word = palin[k] + palin[q]
    #         reverse = word[::-1]
    #         if word == reverse:
    #             answer.append(word)
    #             PLAG = False
    #             break
    #     if PLAG == False:
    #         break
    if PLAG == True:
        answer.append(0)
for i in range(n):
    print(answer[i])

"""
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    case = int(input())
    li = []
    for i in range(case):
        li.append(input().rstrip())
    P = list(permutations(li, 2))
    answer = []
    for j in P:
        answer.append(''.join(j))
    symbol = False
    for k in answer:
        for q in range(len(k)//2):
            m = 0
            if k[m] == k[len(k)-1-m]:
                m += 1
            else:
                break
        if m == (len(k)//2):
            print(k)
            sys.exit()
"""

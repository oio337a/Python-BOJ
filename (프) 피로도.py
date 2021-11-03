"""
최소 피로도, 소모 피로도

던전을 최대한 많이 탐험

던전 최대 8!
"""

from itertools import permutations


def solution(k, dungeons):
    answer = []

    per = list(permutations(dungeons, len(dungeons)))

    for i in per:
        count = 0
        piro = k
        for j in range(len(i)):
            if piro >= i[j][0]:
                piro -= i[j][1]
                count += 1
        answer.append(count)
    return max(answer)


solution(80, [[80, 20], [50, 40], [30, 10]])

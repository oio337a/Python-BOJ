"""
가장 많이 겹치는 단품을 course
"""
from itertools import combinations  # 조합
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f]
                       == max(counter.values())]
    return sorted(answer)

# 2,3,4 코스
# orders


"""
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
temp 
ab ac af ag bc 
AC : 2
combination[a, b, c]
"""

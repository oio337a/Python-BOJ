# 문자열 변환
# https://www.acmicpc.net/problem/10453

# 예제의 aabbabab -> aaaabbbb 를 생각해보자.
#
# 편의를 위해 b를 공백으로 생각하고, a만을 움직인다 생각해도 문제는 변함이 없다.
#
# 그렇다면 문제는
#
# aa__a_a_ -> aaaa____
#
# 위와같이 단순화된다.
#
# a는 각각 1,2,5,7의 위치에 있고 이를 각각 1,2,3,4의 위치로 옮겨주기만 하면 된다.
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a_list, b_list = map(list, input().split())
    a_index_list = []
    b_index_list = []
    target = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] == target:
            a_index_list.append(i)
        if b_list[i] == target:
            b_index_list.append(i)
    cnt = 0
    for i in range(len(a_index_list)):
        cnt += abs(a_index_list[i] - b_index_list[i])
    print(cnt)
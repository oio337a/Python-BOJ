'''
S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)을 합쳐서 만들 수 있다.

s(0) = moo

s(1) = s(0) + mo*(3) + s(0)
s(1) = moo + mooo + moo

s(k) = 2 * s(k - 1) + k + 3

s(k) = s(L)
'''
import sys
s0 = ['m', 'o', 'o']


def sol(n, k, l):  # n : 찾을 글자, k : 차수, l : 이전 차수의 길이
    new_l = 2*l + k + 3
    if n <= 3:
        print(s0[n-1])
        sys.exit(0)
    if new_l < n:     # n 이 new_l 클 경우 (new_l 안에 n 을 포함 할 때 까지 재귀)
        sol(n, k+1, new_l)
    else:       # new_l 안에 n 이 포함되는 경우
        if n > l and n <= l + k + 3:
            if n-l != 1:
                print('o')
            else:
                print('m')
            sys.exit(0)
        else:
            # n - (l + k + 3)을 진행해서 다시 첫번째 파트로 돌아온 다음
            # 처음부터 다시 재귀
            sol(n - (l + k + 3), 1, 3)


n = int(input())
sol(n, 1, 3)

'''
g = lambda i:(i << 2) - bin(i).count('1')
i = int(input())-1
n = max((i//4)-9, 0)
while g(n) < i : n += 1
print('om'[g(n)==i])
'''


def change(n, k):  # 진법 변환 함수
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]


def solution(n, k):
    answer = 0
    s = change(n, k)
    s_li = s.split('0')

    # 에라토스테네스의 체
    n = int(max(s_li))

    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    for num in s_li:
        if not num:
            continue
        if int(num) in primes:
            answer += 1
    return answer


n = 110011
k = 10
print(solution(n, k))

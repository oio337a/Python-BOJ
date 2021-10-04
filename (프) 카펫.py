def solution(b, y):
    s = b + y
    for i in range(s, 2, -1):
        if s % i == 0:
            a = s // i
            if y == (i-2)*(a-2):
                return [i, a]

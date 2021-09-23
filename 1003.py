"""
f(n) = f(n-1) + f(n-2)
1 0 f(0) = f(0) = 0      
0 1 f(1) = f(1) = 1
1 1 f(2) = f(1) + f(0)
1 2 f(3) = f(1) + f(0) + f(1)
2 3 f(4) = f(1) + f(0) + f(1) + f(1) + f(0)
3 5 f(5) = f(1) + f(0) + f(1) + f(1) + f(0) + f(1) + f(0) + f(1)
5 8 f(6) = f(1) + f(0) + f(1) + f(1) + f(0) + f(1) + f(0) + f(1) + f(1) + f(0) + f(1) + f(1) + f(0)"""

import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(f"{zero[num]} {one[num]}")


n = int(input())

for _ in range(n):
    fibo(int(input()))

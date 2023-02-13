# 밑수의 n 승 법칙

a = []
b = []
T = int(input())

for i in range(T):
    num1, num2 = input().split()
    a.append(int(num1))
    b.append(int(num2))

for x in range(T):
    base = a[x] % 10  # 밑수 구하기

    if base == 0:  # 0인 경우
        print(10)
    elif base in [1, 5, 6]:  # 1, 5, 6 인 경우
        print(base)
    elif base in [4, 9]:  # 4, 9 인 경우
        if b[x] % 2 == 0:  # 짝수
            print(base**2 % 10)
        else:  # 홀수
            print(base)
    else:  # 2, 3, 7, 8 의 경우
        if b[x] % 4 == 0:
            print(base**4 % 10)
        else:
            print(base**(b[x] % 4) % 10)

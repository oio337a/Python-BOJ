def beasu(N, num):
    if len(N) > 1:
        num += 1
        t = 0
        for i in N:
            t += int(i)
        beasu(str(t), num)
    else:
        if int(N) % 3 == 0:
            print(num)
            print("YES")
        else:
            print(num)
            print("NO")


n = input()
num = 0
beasu(n, num)

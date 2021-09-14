def beasu(aa, num):
    if len(aa) > 1:
        num += 1
        t = 0
        for i in aa:
            t += int(i)
        beasu(str(t), num)
    else:
        if int(aa) % 3 == 0:
            print(num)
            print("YES")
        else:
            print(num)
            print("NO")


n = input()
num = 0
beasu(n, num)


# def func(string, cnt):
#     if len(string) > 1:
#         cnt += 1
#         t = 0
#         for i in string:
#             t += int(i)
#         func(str(t), cnt)
#     else:
#         if int(string) % 3 == 0:
#             print(cnt)
#             print("YES")
#         else:
#             print(cnt)
#             print("NO")


# n = input()
# cnt = 0
# func(n, cnt)

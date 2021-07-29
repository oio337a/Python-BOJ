# A,B,C = map(int,input().split())

# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# A, B = map(int, input().split())

# print(A*(B % 10))
# print(A*(B // 10 % 10))
# print(A*(B//100))
# print(A*B)

# A, B = map(int,input().split())

# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")

# A = int(input())

# if 90 <= A <= 100:
#     print("A")
# elif 80 <= A < 90:
#     print("B")
# elif 70 <= A < 80:
#     print("C")
# elif 60 <= A < 70:
#     print("D")
# else:
#     print("F")

A = int(input())

if (A % 4 == 0 and A % 100 != 0) or A % 400 == 0:
    print(1)
else:
    print(0)

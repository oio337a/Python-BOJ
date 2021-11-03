# """
# 2^1 = 2 10
# 2^2 = 4 100
# 2^3 = 8 1000


# 19 = 10011
# 10100
# 10101

# """


# def solution(numbers):
#     answer = []

#     for num in numbers:
#         if num % 2 == 0:  # 짝수 일 경우
#             binary_num = list(bin(num)[2:])
#             binary_num[-1] = "1"
#         else:
#             binary_num = bin(num)[2:]
#             binary_num = "0" + binary_num
#             idx = binary_num.rfind("0")
#             binary_num = list(binary_num)
#             binary_num[idx] = "1"
#             binary_num[idx + 1] = "0"

#         answer.append(int("".join(binary_num), 2))

#     return answer

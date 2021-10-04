from typing import AnyStr


def solution(phone_number):
    word_len = len(phone_number)
    last = phone_number[word_len - 4:]
    start = '*' * (len(phone_number) - 4)
    answer = start + last
    return answer


print(solution("027778888"))

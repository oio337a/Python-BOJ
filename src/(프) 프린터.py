from collections import deque


def solution(priorities, location):
    answer = 0
    printer = deque([(v, i) for i, v in enumerate(priorities)])

    while (len(printer)):
        item = printer.popleft()
        # 뽑은 item 보다 큰 프린터 물이 있다면
        if printer and max(printer)[0] > item[0]:
            printer.append(item)
        # 뽑은 item 이 제일 중요하다면
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while (left <= right):
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += (mid // time)
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
    return answer


"""
mid 시간 // 1명을 처리하는데 걸리는 시간 = 
한명의 심사관이 mid시간 동안 처리하는 업무 수
"""

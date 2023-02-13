import heapq


def solution(s, k):
    heap = []
    for num in s:
        heapq.heappush(heap, num)
    mix_cnt = 0

    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(
                heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt

# def solution(scoville, k):
#     mix_cnt = 0
#     while min(scoville) < k:
#         scoville.sort()
#     try:
#         scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
#     except IndexError:
#         return -1
#     mix_cnt += 1
#     return mix_cnt


solution([1, 2, 3, 9, 10, 12], 7)

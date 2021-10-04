
def solution(sizes):
    answer = 0

    sizes = [sorted(size, reverse=True) for size in sizes]

    w = [size[0] for size in sizes]
    h = [size[1] for size in sizes]

    w, h = max(w), max(h)

    answer = w * h
    return answer

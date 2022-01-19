from collections import Counter


def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    singo = []

    dict = {id: [] for id in id_list}
    for i in set(reports):
        report = i.split(' ')
        singo.append(report[1])
        dict[report[0]].append(report[1])

    singo = set([i for i in singo if singo.count(i) >= k])

    for key, value in dict.items():
        for s in singo:
            if s in value:
                answer[id_list.index(key)] += 1
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo", "apeach frodo",
           "frodo neo", "muzi neo", "apeach muzi"]
print(solution(id_list, reports, 2))

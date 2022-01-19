
# def solution(id_list, reports, k):
#     answer = [0] * len(id_list)
#     singo = []

#     dict = {id: [] for id in id_list}
#     for i in set(reports):
#         report = i.split(' ')
#         singo.append(report[1])
#         dict[report[0]].append(report[1])

#     singo = set([i for i in singo if singo.count(i) >= k])

#     for key, value in dict.items():
#         for s in singo:
#             if s in value:
#                 answer[id_list.index(key)] += 1
#     return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# reports = ["muzi frodo", "apeach frodo",
#            "frodo neo", "muzi neo", "apeach muzi"]
# print(solution(id_list, reports, 2))

from collections import defaultdict


def solution(id_list, report, k):
    # {'muzi': None, 'frodo': None, 'apeach': None, 'neo': None}
    #iddict = dict.fromkeys(id_list)
    # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0} -> {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    iddict = dict.fromkeys(id_list, 0)
    # {'muzi': [], 'frodo': [], 'apeach': [], 'neo': []} -> {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []}
    maildict = dict([(key, []) for key in id_list])
    # {'muzi': 2, 'frodo': 1, 'apeach': 1, 'neo': 0}
    # dict([(key, []) for key in id_list])
    resultdict = dict.fromkeys(id_list, 0)
    for i in report:
        fromId, toId = i.split()
        # 같은 사람이 여러번 한사람을 신고했을 경우
        if toId in maildict.get(fromId):
            continue
        maildict.get(fromId, []).append(toId)
        iddict[toId] += 1
    for idk, idv in iddict.items():
        if int(idv) >= k:
            for mk, mv in maildict.items():
                if idk in mv:
                    resultdict[mk] += 1
    answer = list(resultdict.values())

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan", "muzi"],
               ["ryan con", "ryan con", "muzi ryan", "muzi con"], 1))

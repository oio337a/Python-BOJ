# from collections import defaultdict
# import math


# def getMin(time):
#     timeLine = time.split(":")
#     nowtime = int(timeLine[0]) * 60 + int(timeLine[1])
#     return nowtime


# def solution(fees, records):
#     numSet = set()
#     for record in records:
#         recordLine = record.split()
#         numSet.add(recordLine[1])

#     # {'0000': [], '5961': [], '0148': []}
#     recordDict = dict([(key, []) for key in numSet])

#     # {'0000': [('06:00', 'IN'), ('06:34', 'OUT'), ('18:59', 'IN')], '5961': [('05:34', 'IN'), ('07:59', 'OUT'), ('22:59', 'IN'), ('23:00', 'OUT')], '0148': [('07:59', 'IN'), ('19:09', 'OUT')]}
#     for record in records:
#         recordLine = record.split()
#         recordDict.get(recordLine[1], []).append(
#             (recordLine[0], recordLine[2]))

#     answer = []
#     for rdictk, rdictv in recordDict.items():
#         total = 0
#         before = 0
#         for index in range(len(rdictv)):
#             if index % 2 == 0:
#                 before = getMin(rdictv[index][0])
#             else:
#                 after = getMin(rdictv[index][0])
#                 gap = after - before
#                 total += gap

#             if index == len(rdictv)-1:
#                 if index % 2 == 0:
#                     gap = 1439 - before
#                     total += gap
#         money = 0
#         if total >= fees[0]:
#             money += fees[1]  # 기본금액
#             total -= fees[0]  # 기본시간 차감

#             rest = math.ceil(total / fees[2])
#             money += rest * fees[3]  # 기본시간 차감
#         else:
#             money = fees[1]
#         answer.append((int(rdictk), int(money)))
#         answer.sort(key=lambda x: x[0])

#     result = []
#     for i in answer:
#         result.append(i[1])
#     #print(result)
#     return result


def time_diff(start_tstr, end_tstr):
    sh, sm = map(int, start_tstr.split(':'))
    eh, em = map(int, end_tstr.split(':'))
    return eh*60 + em - sh*60 - sm


def toll(btime, bfee, atime, afee, tdiff):
    if tdiff <= btime:
        return bfee
    else:
        adiff = (tdiff - btime - 1) // atime + 1
        return bfee + adiff * afee


def solution(fees, records):
    centry = {}
    ctime = {}
    for record in records:
        tstr, car_id, act = record.split(' ')
        if act == 'IN':
            centry[car_id] = tstr
        else:
            if car_id in ctime:
                ctime[car_id] += time_diff(centry[car_id], tstr)
            else:
                ctime[car_id] = time_diff(centry[car_id], tstr)
            centry[car_id] = None

    for car_id, tstr in centry.items():
        if tstr is not None:
            if car_id in ctime:
                ctime[car_id] += time_diff(tstr, '23:59')
            else:
                ctime[car_id] = time_diff(tstr, '23:59')

    return list(map(lambda x: toll(*fees, ctime[x]), sorted(ctime.keys())))

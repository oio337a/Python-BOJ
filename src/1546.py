n = int(input())
li = list(map(int, input().split()))

av = []
num = max(li)

for i in li:
    av.append(i/num*100)

print(sum(av)/len(av))

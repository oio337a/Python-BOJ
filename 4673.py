num_li = set(range(1, 10001))
num_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num_num.add(i)
self_num = sorted(num_li - num_num)
for i in self_num:
    print(i)

'''
def d(a):
    if(a<10):
        return a+a
    elif(a<100):
        return a+a//10+a%10
    elif(a<1000):
        return a+a//100+(a%100)//10+a%10
    else:
        return a+a//1000+(a%1000)//100+(a%100)//10+a%10
a= set()
for i in range(10000):
    a.add(d(i))
for i in range(1,10000):
    if(i not in a):
        print(i)
'''

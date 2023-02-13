from sys import call_tracing


H, W = map(int, input().split())

for _ in range(H):
    s = input()
    c_idx = -1
    for i in range(W):
        if s[i] == 'c':
            c_idx = i
            print(0, end=' ')
        elif c_idx == -1:
            print(-1, end=' ')
        else:
            print(i-c_idx, end=' ')
    print()

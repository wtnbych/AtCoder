N, M = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
B = sum(A)
if N < B:
    print('-1')
else:
    print(N - B)
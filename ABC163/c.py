from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
for i in range(N):
    print(counter[i+1])
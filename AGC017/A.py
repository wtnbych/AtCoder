import itertools
N, P = input().split()
A = list(map(int, input().split()))
even = 0
for i in A:
    if i % 2 == 0:
        even += 1
odd = int(N) - even
even_list = range(even)
odd_list = range(odd)



'''
if int(P) == 0:
    ans = 1
else:
    ans = 0
for i in range(int(N)):
    for j in itertools.combinations(A, i+1):
        if sum(j)%2 == int(P):
            ans += 1
print(ans)
'''
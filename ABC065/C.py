import sys
sys.setrecursionlimit(2 ** 30)

def fact(n):
    if n == 0: return 1
    return n * fact(n-1)

N, M=map(int,input().split())
if(abs(N%1000000007-M%1000000007)>1):
    i=0
else:
    i=fact(M%1000000007)*fact(N%1000000007)
if(N==M):
    i=i*2
ans=i%1000000007
print(ans)
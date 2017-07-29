N=int(input())
a=list(int(input()) for i in range(N))
j=0
i=1
while j < N:
    i=a[i-1]
    j+=1
    if(i==2):
        print(j)
        break
else:
    print("-1")
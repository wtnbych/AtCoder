n = int(input())
a = list(map(int, input().split()))
b = list()
c = list()
for i in range(n):
    if(i==0):
        b.append(a[i])
    elif(i%2==1):
        b.append(a[i])
    else:
        c.append(a[i])
c.reverse()
c = c + b
if(i%2==1):
    c.reverse()
for i in c:
    print(i,end=' ')
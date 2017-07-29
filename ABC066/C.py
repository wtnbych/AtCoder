n = int(input())
a = list(input().split())
b = ""
for i in range(n):
    if(i==0):
        b = str(a[i])
    elif(i%2==1):
        b = str(b) + str(a[i])
    else:
        b = str(a[i]) + str(b)
if(i%2==1):
    b = b[::-1]
for i in range(n):
    print(b[i],end=' ')
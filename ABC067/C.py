N = int(input())
a = list(map(int, input().split()))
sunuke = []
diff = []
total = sum(a)
for i, x in enumerate(a[0:-1]):
    if(i==0):
        sunuke.append(x)
    else:
        sunuke.append(x + sunuke[i-1])
for i in sunuke:
    diff.append(abs((i * 2) - total))
print(min(diff))

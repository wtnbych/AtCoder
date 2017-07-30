N = int(input())

A = [64,32,16,8,4,2]
if N<2:
    print(1)
else:
    for i in A:
        if N >= i:
            break
    print(i)
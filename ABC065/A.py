X, A, B = map(int, input().split())
if B-A>X:
    print("dangerous")
elif A>=B:
    print("delicious")
else:
    print("safe")
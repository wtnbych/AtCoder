r, g, b = map(str, input().split())
if int(r+g+b, 10)%4==0:
    print("YES")
else:
    print("NO")
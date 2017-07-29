N = int(input())
a = list(map(int, input().split()))
gray = 0
brown = 0
green = 0
sky = 0
blue = 0
yellow = 0
orange = 0
red = 0
god = 0
for i in range(N):
    if a[i] < 400:
        gray = 1
    elif a[i] < 800:
        brown = 1
    elif a[i] < 1200:
        green = 1
    elif a[i] < 1600:
        sky = 1
    elif a[i] < 2000:
        blue = 1
    elif a[i] < 2400:
        yellow = 1
    elif a[i] < 2800:
        orange = 1
    elif a[i] < 3200:
        red = 1
    else:
        god+=1
zako = gray + brown + green + sky + blue + yellow + orange + red
if god > 0 and zako == 0:
    color_max = god
    color_min = 1
elif god > 0 and zako != 0:
    color_max = zako + god
    color_min = zako
else:
    color_max = zako
    color_min = zako
print(color_min, color_max)
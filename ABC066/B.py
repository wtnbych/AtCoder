S = input()
L = len(S)
if(L%2!=0):
    L-=1
else:
    L-=2
for i in range(L,0,-2):
    if(S[0:(i//2)]==S[(i//2):i]):
        print(i)
        break
else:
    print("0")
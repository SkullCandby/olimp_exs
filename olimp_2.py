X, Y, N = int(input()), int(input()), int(input())
c = (N // (X + Y)) * 2
ost = N % (X + Y)

if ost == 0:
    print(c)
elif (ost <= X or ost <= Y) and ost != 0:
    print(c + 1)
else:
    print(c + 2)

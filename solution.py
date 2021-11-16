def task2(self):
    X, Y, N = int(input()), int(input()), int(input())
    c = (N // (X + Y)) * 2
    ost = N % (X + Y)
    if ost == 0:
        print(c)
    else:
        print(c + ost)


def task3(self):
    S, F, N = int(input()), int(input()), int(input())
    mx1 = 10 ** 9
    mx2 = 10 ** 9
    for j in range(N):
        E = int(input())
        mx1 = min(mx1, abs(S - E))
        mx2 = min(mx2, abs(F - E))
    if abs(S - F) < abs(mx1 + mx2 + 1):
        print(abs(S - F))
    else:
        print(abs(mx1 + mx2 + 1))
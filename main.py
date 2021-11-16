class Olimp:
    def task1(self):
        N, K = int(input()), int(input())
        if K == N:
            print(0)
        else:
            N //= K
            print(2 * N * (N - 1) * K)

    def task2(self):
        X, Y, N = int(input()), int(input()), int(input())
        c = (N // (X + Y)) * 2
        ost = N % (X + Y)

        if ost == 0:
            print(c)
        elif (ost <= X or ost <= Y) and ost != 0:
            print(c + 1)
        else:
            print(c + 2)

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
    def task4(self):
        N, L = int(input()), int(input())
        arr = [1]
        for i in range(N - 1):
            arr.append(0)
        for i in range(N):
            F = int(input())
            if arr[i] == 1:
                for e in range(i, i + int(F / L + 1)):
                    arr[e] = 1
        for i in range(N - 1, -1, -1):
            if arr[i] == 1:
                print(i + 1)
                break
    def task5(self):
        X, Y = int(input()), int(input())
        if X == Y:
            print(-1)
        elif Y >= (X*2 - 1):
            print(X)
        else:
            K = X*2 - Y
            C = Y - X + 1
            if K == C:
                print(X * (2 + K // C - 1))
            else:
                print(X * (2 + K // C))


olimp = Olimp()

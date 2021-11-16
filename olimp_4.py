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

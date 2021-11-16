n = int(input())
k = int(input())

if n == k:
    print(0)
else:
    n = n//k
    print((n-1) * n + (n-1) * n)
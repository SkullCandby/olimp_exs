a = int(input())
b = int(input())
av = []
mn = a * 2
mx = 2 * b
if mx + 1 - a < mn:
    print(-1)
else:
    print(mn)
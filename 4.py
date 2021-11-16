m = int(input())
arr = []
for i in range(3):
    arr.append(int(input()))
min_ = min(arr)
max_ = max(arr)
cntr = 0
for i in range(m-3):
    d = int(input())
    if not(min_ <= d <= max_):
        cntr += 1
print(cntr)
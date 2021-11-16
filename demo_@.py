a = int(input())
b = int(input())

n_op = (a + b) / 3
arr =[]

n_op = int(n_op)
for i in range(1, n_op + 1):
    k1_e2 = i
    k2_e1 = n_op - i
    if a - 1 * k1_e2 - 2 * k2_e1 == 0 and b - k1_e2 * 2 - k2_e1 * 1 == 0:
        arr.append((k2_e1, k1_e2))

print(-1) if len(arr) == 0 else print(arr[0][0], arr[0][1])
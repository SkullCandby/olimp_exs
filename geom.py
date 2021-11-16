'''import math
b = 1982
a = 0
c = 0
print(math.sin(90))
dd = {}
dd2 = {}
for i in range(0, 120+1):
    dd[i] = b * math.sin(i) / math.sin(60)
    dd2[120-i] = b * math.sin(120 - i) / math.sin(60)
lst = []
lst2 = []
[lst.append(values) for values in dd.values()]
[lst2.append(values) for values in dd2.values()]
new_lst = []
for i in range(len(lst)):
    if lst[i] == int(lst[i]):
        new_lst.append(lst[i])
print(new_lst)
max = 0
for i in range(len(lst)):
    if (lst[i] + lst2[len(lst2) - 1 - i] + 1982) >= max:
        max = lst[i] + lst2[len(lst2) - 1 - i] + 1982'''

print(eval(input()))

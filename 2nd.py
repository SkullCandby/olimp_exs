# https://acmp.ru/index.asp?main=task&id_task=2
s = 0
a = int(input())

if a > 0:
    print(int((1 + a) / 2 * abs(a)))
elif a <= 0:
    print(int((1 + a) / 2 * (abs(a) + 2)))
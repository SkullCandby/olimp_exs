def rectRect(a, b):
    # r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h
    r1x = int(a[0])
    r1y = int(a[1])
    r1w = int(a[2]) - int(a[0])
    r1h = int(a[3]) - int(a[1])
    r2x = int(b[0])
    r2y = int(b[1])
    r2w = int(b[2]) - int(b[0])
    r2h = int(b[3]) - int(b[1])
    # are the sides of one rectangle touching the other?

    return r1x + r1w >= r2x and r1x <= r2x + r2w and r1y + r1h >= r2y and r1y <= r2y + r2h


# print(rectRect(1, 1, 1, 9, 3, 1, 7, 2))

def ploschad(a):
    r1w = int(a[2]) - int(a[0])
    r1h = int(a[3]) - int(a[1])
    return r1w * r1h


def can_or_not(pos1, pos2):
    if pos1 != None:
        dd = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8
              }
        pos1_ = (dd[pos1[0]], dd[pos1[1]])
        pos2_ = (dd[pos2[0]], dd[pos2[1]])
        if (abs(pos1_[0] - pos2_[0])) == (abs(pos1_[1] - pos2_[1])) or (pos1_[0] == pos2_[0]) or (pos1_[1] == pos2_[1]):
            arg1 = True
            arg2 = pos2
            return (arg1, arg2)
        else:
            return (False, 0)
    else:
        return (False, 0)

class bmstu_olimp:
    def task_1(self):
        a = input()
        cntr = 0
        arr = []
        start_element = a[0]
        for i in range(len(a)):
            try:
                if int(start_element + a[i + 1]) % 5 == 0 and start_element != '0':
                    arr.append(int(start_element + a[i + 1]))
                start_element = a[i + 1]
            except IndexError:
                pass
        print(len(arr))

    def task_2(self):
        a = input().split()
        ans = ''

        def toBASEint(num, base):
            alpha = "0123456789"
            n = abs(num)
            b = alpha[n % base]
            while n >= base:
                n = n // base
                b += alpha[n % base]
            return ('' if num >= 0 else '-') + b[::-1]

        def toBaseFrac(frac, base, n=10):
            alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            b = ''
            while n:
                frac *= base
                frac = round(frac, n)
                b += str(int(frac))
                frac -= int(frac)
                n -= 1
            return b

        Number = a[0]
        ogr = int(a[1])
        Basein = 10
        Baseout = 4
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if '.' in Number:
            num, frac = map(str, Number.split('.'))
            num = int(num, Basein)
            a = toBASEint(num, Baseout)
            b = 0
            k = Basein
            for i in frac:
                b += alpha.index(i) / k
                k *= Basein
            b = toBaseFrac(b, Baseout)
            ans = a + '.' + b
        else:
            ans = toBASEint(int(Number, Basein), Baseout)
        ans = ans[:ogr + 2]
        a = len(ans)
        for i in range(a, 0, -1):
            try:
                if ans[i] == '0' and ans[i - 1] == '0':
                    ans = ans[:i - 1]
            except IndexError:
                pass
        print(ans)

    def task_3(self):
        dd = {}
        n = int(input())
        arr = []

        for i in range(n):
            arr.append(input().split())
        for i in range(n):
            dep = arr[i]
            dd[i] = ploschad(dep)
            for j in range(n):
                if i != j:
                    if rectRect(dep, arr[j]):
                        dd[i] += ploschad(arr[j])
        print(max(dd.values()))

    def task_4(self):
        n = int(input())
        arr = []

        for i in range(n):
            arr.append(input().split())
        for i in range(n):
            print('\t'.join(arr[i]))

    def task_5(self):
        dd = {}
        n = int(input())
        arr = []

        for i in range(n):
            arr.append(input().split())
        m = int(input())
        for i in range(n):
            lost_money = int(arr[i][0])
            zabol = int(arr[i][1]) * int(arr[i][2]) // 100
            dep = arr[i]
            new_arr = []
            new_arr.append(i + 1)

            for j in range(n):
                if i != j:
                    if zabol < m:
                        zabol += (int(arr[j][1]) * int(arr[j][2]) // 100)
                        new_arr.append(j + 1)
                        lost_money += int(arr[j][0])
            dd[' '.join(str(x) for x in new_arr)] = lost_money

        min_magaz = list(range(0, n))
        min_sum = 0
        for i in range(n):
            min_sum += int(arr[i][0])
        for value, item in dd.items():
            if item < min_sum:
                min_sum = item
                min_magaz = value
            elif item == min_sum:
                if len(value) < len(min_magaz):
                    min_magaz = value
                elif len(value) == len(min_magaz):
                    a = value.split()
                    [int(x) for x in a]
                    a.sort()
                    min_magaz = a

        print(*min_magaz)

    def task_6(self):
        dd = {}
        dd_start = {}
        n_ = input().split()
        n = int(n_[0])
        START = n_[1]
        arr = []
        print(START)
        for i in range(n):
            a = input()
            arr.append(a)
            dd[a] = []

        for i in range(n):
            new_arr = []
            for j in range(n):
                try:
                    ans = can_or_not(dd_start[arr[i]], arr[j])
                    print(ans, 't')
                except KeyError:
                    ans = can_or_not(START, arr[j])
                    print(ans, 'e', arr[j])
                print(dd_start)
                if ans[0]:

                    dd_start[arr[i]] = ans[1]
                    dd[arr[i]].append(arr[j])

            #dd[len(new_arr)] = new_arr
        print(dd_start)
        print(dd)
        max_way = 0
        max_arr = []
        """for item, value in dd.items():
            if item > max_way:
                max_way = item
                max_arr = value
        print(max_way)
        [print(x) for x in max_arr]"""


ol = bmstu_olimp()
print(can_or_not('H2', 'C5'))
ol.task_6()

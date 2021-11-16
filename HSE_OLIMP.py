import math

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return int(x), int(y)
    else:
        return False
def get_diag(pos1, pos2, pos3, pos4):
    arr = []
    if pos3 > pos1:
        pos1_ = pos1 - 1
        pos3_ = pos3 + 1
        pos2_ = pos2 + 1
        pos4_ = pos4 + 1
    if pos3 < pos1:

        pos1_ = pos1 - 1
        pos3_ = pos3 + 1
        pos2_ = pos2 + 1
        pos4_ = pos4 + 1
    if pos3 == pos1:
        if pos2 < pos4:
            pos1_ = pos1 + 1
            pos3_ = pos3 + 1
            pos2_ = pos2 + 1
            pos4_ = pos4 - 1
        if pos2 > pos4:
            pos1_ = pos1 + 1
            pos3_ = pos3 + 1
            pos2_ = pos2 - 1
            pos4_ = pos4 + 1
        if pos2 == pos4:
            pos1_ = pos1
            pos2_ = pos2
            pos3_ = pos3
            pos4_ = pos4
    l1 = line([pos1, pos2], [pos1_, pos2_])
    l2 = line([pos3, pos4], [pos3_, pos4_])
    arr.append(intersection(l1, l2))
    arr.append((pos3, pos4))
    return arr

class HSE_OLIMP:
    def task1(self):
        a = [int(x) for x in input().split()]
        start = (a[0], a[1])
        end = (a[2], a[3])
        first = (start[0] + start[1]) % 2
        second = (end[0] + end[1]) % 2
        if first == 1 and second == 0:
            print(-1)
        elif first == 1 and second == 1:
            if (start[0] - start[1]) == (end[0] - end[1]) or (start[0] + start[1]) == (end[0] + end[1]):
                print(1)
                print(end[0], end[1])
            else:
                a = get_diag(start[0], start[1], end[0], end[1])
                print(2)
                for i in range(2):
                    print(a[i][0], a[i][1])
        elif first == 0 and second == 0:
            print(-1)
        elif first == 0 and second == 1:
            able_arr = []
            x = start[0]
            y = start[1]
            able_arr = [(x + 1, y - 2), (x + 1, y + 2), (x - 1, y + 2), (x - 1, y - 2,), (x + 2, y - 1), (x + 2, y + 1),
                        (x - 2, y - 1), (x - 2, y + 1)]
            res = []

            try:
                if able_arr.index((end[0], end[1])) != -1:
                    print(1)
                    print(end[0], end[1])
            except ValueError:
                flag = False
                for i in range(len(able_arr)):
                    if able_arr[i][0] >= 0 and able_arr[i][1] >= 0:
                        if (able_arr[i][0] - able_arr[i][1]) == (end[0] - end[1]) or (able_arr[i][0] + able_arr[i][1]) == (end[0] + end[1]):
                            print(2)
                            print(able_arr[i][0], able_arr[i][1])
                            print(end[0], end[1])
                            flag = True
                            break
                        else:
                            res_ = get_diag(able_arr[i][0], able_arr[i][1], end[0], end[1])
                            a = (able_arr[i][0], able_arr[i][1])
                            res_.append(a)
                            res.append(res_)
                if not flag:
                    print(3)
                    print(res[0][-1][0], res[0][-1][1])
                    for i in range(2):
                        print(res[0][i][0], res[0][i][1])


hse = HSE_OLIMP()
hse.task1()

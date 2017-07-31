import math
in_case = input()

x1, y1, r1, x2, y2, r2 = [], [], [], [], [], []

for _ in range(int(in_case)):
    in_x1, in_y1, in_r1, in_x2, in_y2, in_r2 = input().split()

    x1.append(in_x1)
    x2.append(in_x2)
    y1.append(in_y1)
    y2.append(in_y2)
    r1.append(in_r1)
    r2.append(in_r2)

for i in range(int(in_case)):

    in_x1 = float(x1[i])
    in_y1 = float(y1[i])
    in_r1 = float(r1[i])
    in_x2 = float(x2[i])
    in_y2 = float(y2[i])
    in_r2 = float(r2[i])

    d = math.sqrt((in_x1-in_x2)**2+(in_y1-in_y2)**2)

    if d > in_r1+in_r2:
        print(0)

    elif d == in_r1+in_r2:
        print(1)

    elif abs(in_r1-in_r2) < d < in_r1+in_r2:
        print(2)

    elif d == abs(in_r1-in_r2):
        print(1)

    elif d < abs(in_r1-in_r2):
        print(0)

    else:
        if in_r1 == in_r2:
            print(-1)

        else:
            print(0)
import math

num_case = int(input())

answer_list = []

for _ in range(num_case):

    x1, y1, x2, y2 = input().split()

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    num_planet = int(input())

    planet_x_list = []
    planet_y_list = []
    planet_r_list = []

    is_included = []

    for _ in range(num_planet):
        planet_x, planet_y, planet_r = input().split()

        planet_x_list.append(float(planet_x))
        planet_y_list.append(float(planet_y))
        planet_r_list.append(float(planet_r))

        is_included.append([0,0])

    for i in range(num_planet):
        d1 = math.sqrt((x1-planet_x_list[i])**2 + (y1-planet_y_list[i])**2)
        d2 = math.sqrt((x2-planet_x_list[i])**2 + (y2-planet_y_list[i])**2)

        if d1 < planet_r_list[i]:
            is_included[i][0] = 1

        if d2 < planet_r_list[i]:
            is_included[i][1] = 1

    result = 0

    for i in is_included:

        if (i[0] == 1 and i[1]==0) or (i[1] == 1 and i[0] == 0):
            result += 1

    answer_list.append(result)

for i in answer_list:
    print(i, end=" ")
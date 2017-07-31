num_case = int(input())

a = [1,2,3,4]

for _ in range(num_case):
    num_building, num_rule = input().split()
    num_building = int(num_building)
    num_rule = int(num_rule)

    build_time = input().split()
    build_time = [int(time) for time in build_time]

    rule_graph = []

    for _ in range(num_building):
        rule_graph.append([])

    for _ in range(num_rule):
        rule = input().split()
        rule = [int(i) for i in rule]
        rule = rule[::-1]

        rule_graph[rule[0]-1].append(rule[1]-1)

    temp = []

    print(rule_graph)
    target_number = int(input())

    def calculate(a, index):

        print(a, index)

        if not a:
            return

        else:
            for i in a:
                global build_time

                if build_time[i] < build_time[i] + build_time[index]:

                    build_time[i] = build_time[i] + build_time[index]

                    print(build_time)

            for i in a:
                calculate(rule_graph[i], i)

    calculate(rule_graph[target_number-1], target_number-1)
    print(build_time[0])

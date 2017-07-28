num = input()
in_ox = []

for i in range(int(num)):
    in_ox.append(input())


for _, string in enumerate(in_ox):
    string = list(string)

    logits = []
    total_num = 0

    for _, c in enumerate(string):
        if c == 'O':
            logits.append(True)

            for _, c in enumerate(logits):
                total_num += 1

        else:
            logits = []


    print(total_num)

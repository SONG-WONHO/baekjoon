import sys
sys.setrecursionlimit(10**6)

num = int(input())

mem = [-1]*(10**6 + 1)
mem[1] = 0
mem[2] = 1
mem[3] = 1


def count_operation(number):
    number = int(number)

    if mem[number] != -1:
        return mem[number]

    else:
        logits = []

        logits.append(count_operation(number - 1) + 1)

        if number%2 == 0:
            logits.append(count_operation(number/2) + 1)

        if number%3 == 0:
            logits.append(count_operation(number/3) + 1)

        mem[number] = min(logits)

        return mem[number]

print(count_operation(num))
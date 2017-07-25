#han_number function
def han_num(num):
    logits = []

    while int(num / 10) != 0:
        logits.append(num % 10)
        num = int(num / 10)

    logits.append(num)
    logits.reverse()

    if len(logits) < 3:
        return 1

    else:
        for i in range(len(logits)-2):
            if logits[i] - logits[i+1] != logits[i+1] - logits[i+2]:
                return 0

        return 1

#input
in_num = input()

#result
result = 0

for i in range(int(in_num)):
    result += han_num(i+1)

#output
print(result)

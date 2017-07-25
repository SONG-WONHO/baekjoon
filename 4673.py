#function
def d(num):
    real_num = num

    while int(num / 10) != 0:
        real_num += num % 10
        num = int(num / 10)

    real_num += num

    return real_num

#decision self_number
logits = []

for i in range(10000):
    logits.append(True)

for i in range(10000):
    temp = d(i+1)

    if temp < 10000:
        #non self_number
        logits[temp-1] = False

for i in range(9999):
    if logits[i] == True:
        print(i+1)

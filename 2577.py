in_num1 = input()
in_num2 = input()
in_num3 = input()

logits = []

for i in range(10):
    logits.append(0)

result = int(in_num1)*int(in_num2)*int(in_num3)
result = list(str(result))

for i in range(len(result)):
    if result[i] == '0':
        logits[0] +=1
    elif result[i] =='1':
        logits[1] +=1
    elif result[i] =='2':
        logits[2] +=1
    elif result[i] =='3':
        logits[3] +=1
    elif result[i] =='4':
        logits[4] +=1
    elif result[i] =='5':
        logits[5] +=1
    elif result[i] =='6':
        logits[6] +=1
    elif result[i] =='7':
        logits[7] +=1
    elif result[i] =='8':
        logits[8] +=1
    elif result[i] =='9':
        logits[9] +=1

for i in range(10):
    print(logits[i])

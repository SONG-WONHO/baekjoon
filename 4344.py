total_case = int(input())

result_list = []

for _ in range(total_case):
    logits = []
    string = input().split()

    num_student = int(string[0])
    score = string[1:]

    for i in range(num_student):
        score[i] = float(score[i])
        logits.append(0)

    mean = sum(score)/num_student

    for i in range(num_student):
        if score[i] > mean:
            logits[i] = 1

    result = sum(logits)/num_student*100
    result_list.append(result)

for i in range(total_case):
    print('%.3f'%result_list[i]+'%')




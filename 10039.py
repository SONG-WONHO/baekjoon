def out_mean(score_list):
    total = 0

    for i in score_list:
        total += i

    return total/len(score_list)

student_num = 5

score_list = []

for _ in range(student_num):
    score = input()
    score_list.append(score)

for i,c in enumerate(score_list):
    if int(c) < 40:
        score_list[i] = "40"

score_list = [int(i) for i in score_list]

print(int(out_mean(score_list)))

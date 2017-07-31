num_case = int(input())

logits = 0

for _ in range(num_case):
    string = str(input())

    string_list = list(string)

    idx2char = list(set(string))

    num_change = 0

    for i in range(len(string_list)-1):
        if string_list[i] != string_list[i+1]:
            num_change += 1

    if len(idx2char) -1 == num_change:
        logits += 1

print(logits)

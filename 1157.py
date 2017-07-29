in_str = input()

in_str = in_str.lower()

idx2char = list(set(in_str))
char2idx = {c:0 for c in idx2char}

for i in range(len(in_str)):
    char2idx[in_str[i]] += 1

logits = 0
max_num = 0

for c in idx2char:
    if max_num < char2idx[c]:
        max_num = char2idx[c]

    elif max_num == char2idx[c]:
        logits = 1
        break

if logits == 1:
    print("?")
else:
    print(max_num)
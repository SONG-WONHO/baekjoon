in_str = str(input())

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

for c in idx2char:
    if max_num == char2idx[c]:
        logits += 1


if logits >= 2:
    print("?")
else:
    for c in idx2char:
        if max_num == char2idx[c]:
            print(c.upper())

alphabet = "abcdefghijklmnopqrstuvwxyz"

in_str = input()

for c in alphabet:
    logits = 0

    for i, k in enumerate(in_str):
        if c == k:
            print(i, end=" ")
            logits = 1
            break

    if logits == 0:
        print(-1, end=" ")

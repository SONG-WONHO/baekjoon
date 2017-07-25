in_str = input()
in_str = list(in_str)

num = 1

for i in range(len(in_str)):
    if in_str[i] == ' ':
        num += 1

print(num)

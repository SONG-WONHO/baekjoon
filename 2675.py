num = input()

str_list = []

for _ in range(int(num)):
    input_str = input()

    str_list.append(input_str)

for c in str_list:
    pasre_num = c[0]
    parse_str = c[2:]

    result = ""
    for k in parse_str:
        result += k*int(pasre_num)

    print(result)

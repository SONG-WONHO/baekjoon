num = int(input())

str_list = []

for _ in range(num):
    input_str = str(input())

    str_list.append(input_str)

for string in str_list:
    pasre_num = string[0]
    parse_str = string[2:]

    result = ""
    for k in parse_str:
        result += k*int(pasre_num)

    print(result)

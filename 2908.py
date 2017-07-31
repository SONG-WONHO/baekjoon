in_num1, in_num2 = input().split()

in_num1 = in_num1[::-1]
in_num2 = in_num2[::-1]

if int(in_num1) > int(in_num2):
    print(int(in_num1))
else:
    print(int(in_num2))
     
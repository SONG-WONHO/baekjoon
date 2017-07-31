#dynamic programming

#input_case
in_case = int(input())

num_list = []

for _ in range(in_case):

    #input_number
    num = int(input())
    num_list.append(num)

for num in num_list:

    #number of count
    num_zero_list = [-1]*41
    num_one_list = [-1]*41

    #case 0
    def fibonacci_zero(num):

        if num == 0:
            return 1

        elif num == 1:
            return 0

        elif num_zero_list[num] != -1:
            return num_zero_list[num]

        else:
            num_zero_list[num] = fibonacci_zero(num-1) + fibonacci_zero(num-2)
            return num_zero_list[num]

    #case 1
    def fibonacci_one(num):

        if num == 0:
            return 0

        elif num == 1:
            return 1

        elif num_one_list[num] != -1:
            return num_one_list[num]

        else:
            num_one_list[num] = fibonacci_one(num-1) + fibonacci_one(num-2)
            return num_one_list[num]

    print(fibonacci_zero(num),fibonacci_one(num))

"""
recursion

in_case = int(input())

num_list = []

for _ in range(in_case):
    num = int(input())
    num_list.append(num)

for num in num_list:
    num_zero = 0
    num_one = 0

    def fibonacci(num):
        if num == 0:
            global num_zero
            num_zero += 1
            return 0

        elif num == 1:
            global num_one
            num_one += 1
            return 1

        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    fibonacci(num)

    print(num_zero, num_one)

if we use recursion, we would have time-out
"""

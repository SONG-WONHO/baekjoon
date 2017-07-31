cro_char_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

string = str(input())

num = 0
logits =0

def is_include(st):
    for c in cro_char_list:
        if c == st:
            return True

    return False

while num < len(string):
    if is_include(string[num:num+2]):
        logits += 1
        num += 2

    elif is_include(string[num:num+3]):
        logits += 1
        num += 3

    else:
        logits += 1
        num += 1

print(logits)

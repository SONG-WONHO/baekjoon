in_str = input()
a = in_str.split()
print(a)
if in_str == "1 2 3 4 5 6 7 8":
    print("ascending")

elif in_str == "8 7 6 5 4 3 2 1":
    print("descending")

else:
    print("mixed")

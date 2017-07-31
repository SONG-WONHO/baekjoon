n, x = input().split()

n = int(n)
x = int(x)

an = input().split()

an = [int(num) for num in an]

for i in range(len(an)):
    if an[i] < x:
        print(an[i], end=" ")
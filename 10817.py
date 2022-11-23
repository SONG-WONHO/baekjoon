"""
Prob) 세 정수가 주어졌을 때, 두 번째로 큰 정수 출력
Ex) 
    Inp: 20 30 10
    Oup: 20
Sol0)
    세 정수를 정렬하고, 중간 출력
"""

nums = map(int, str(input()).split(" "))
print(sorted(nums)[1])

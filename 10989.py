"""
Prob) N개의 수가 주어졌을 때, 이를 오름차순으로 정렬
Ex) 
    Inp: 20 30 10
    Oup: 10 20 30
Sol0)
    파이썬의 sorted 함수를 사용
Sol1)
    병합정렬을 직접 구현해서 사용
Sol2)
    퀵정렬을 직접 구현해서 사용
Hint)
    - 메모리 제한 존재
    - 들어오는 수는 10,000보다 작거나 같은 자연수
Sol3)
    개수를 세서 정렬
"""
import sys


counting = [0] * 10001

n = int(sys.stdin.readline())

for _ in range(n):
    counting[int(sys.stdin.readline())] += 1

for index in range(10001):
    if counting[index] != 0:
        for _ in range(counting[index]):
            print(index)

"""
Prob: N개의 정수가 주어졌을 때, X라는 정수가 존재하는지 알아내라
Ex: 
    Inp: 
        A: 4 1 5 2 3
        B: 1 3 5 5 7
    Oup: 
        True, True, True, True, False
Sol0:
    1. 가장 무식한 방법은 B의 각 원소별로 A에 존재하는지 찾기
    2. 찾는 것도 A의 처음부터 끝까지 순회
    -> O(B*A)
Sol1:
    1. 찾는 것을 처음부터 끝까지 순회하는게 아니라 이진서치를 하면 어쩔까?
    -> O(B*logA)
Sol2:
    1. 앞에서 찾은 결과를 이용할 수도
    2. 같은 숫자의 경우 찾아놓으면 장땡
    3. 따라서 미리 해쉬테이블을 구성
    4. 이후 B는 해쉬테이블을 조회
    -> O(A + B*1)
    -> O(A + B)
Sol3:
    1. 해쉬테이블을 만들 때 이진탐색을 할 수 있지 않을까?
    -> O(logA + B*1)
    -> O(logA + B)
"""
import sys
from collections import defaultdict


n = int(sys.stdin.readline())
ref = defaultdict(int)
for num in str(sys.stdin.readline()).strip().split(" "):
    ref[int(num)] = True

n = int(sys.stdin.readline())
query = str(sys.stdin.readline()).strip().split(" ")
for num in query:
    if ref.get(int(num)):
        print(1)
    else:
        print(0)

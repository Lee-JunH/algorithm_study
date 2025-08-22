"""
SWEA_18544 - 전위순회 - D2

문제
- 간선 정보가 주어졌을 때 전위순회하여 정점의 번호를 출력하시오

풀이
- 전위순회하기
"""

from collections import deque

V = int(input())
lst = list(map(int, input().split()))
my_dict = {}
for i in range(0, len(lst), 2):
    a, b = lst[i], lst[i+1]
    my_dict.setdefault(a, [])
    my_dict[a].append(b)
my_q = deque()
my_q.append(min(lst))
result = [min(lst)]

def preorder():
    while my_q:
        temp = my_q.popleft()
        if temp in my_dict:
            for n in my_dict[temp]:
                my_q.append(n)
                result.append(n)
                preorder()
preorder()
print(*result)
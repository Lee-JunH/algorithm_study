"""
SWEA_1244 - 최대 상금 - D3

문제
- 주어진 숫자판들 중에 두 개를 선택해서 정해진 횟수만큼 서로의 자리를 교환할 수 있다.
- 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액
"""

def str_to_num(stack):
    i = 0
    num = 0
    stack.reverse()
    while i < len(stack):
        num += int(stack[i]) * (10 ** i)
        i += 1
    stack.reverse()
    return num

def swap_num(a, b):
    number[a], number[b] = number[b], number[a]

def find_max_index(index):
    max_v = max(number[index+1:])
    for i in range(length-1, index-1, -1):
        if number[i] == max_v:
            return i

def dfs(s):
    global max_num

    if s == swap:
        my_num = str_to_num(number)
        if max_num < my_num:
            max_num = my_num
        return
    
    for i in range(length-1):
        j = find_max_index(i)
        swap_num(i, j)  # 자리 바꾸기
        dfs(s+1)
        swap_num(i, j)  # 원래대로

T = int(input())
for case in range(T):
    number, swap = map(int, input().split())
    number = list(str(number).strip())
    
    max_num = 0
    length = len(number)
    dfs(0)

    print(f'#{case+1} {max_num}')
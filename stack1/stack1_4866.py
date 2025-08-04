"""
swea_4866 - 괄호검사 - D2

문제 설명 - {(({}))}
각 쌍이 제대로 맞는지 확인하는 문제
"""

T = int(input())

for case in range(T):
    code = input()

    correct = 1
    lst = []
    for s in code:
        if s == '(' or s == '{':    # 괄호를 열 때는 리스트에 추가(push)
            lst.append(s)
        elif s == ')' or s == '}':  # 괄호를 닫을 때
            if len(lst) == 0:       # 리스트에 짝이 아무것도 없는 경우 오류!
                correct = 0
                break

            temp = lst.pop()        # 리스트에 있는 짝이 맞는지 보기 위해 pop
            if (s == ')' and temp != '(') or (s == '}' and temp != '}'): # 짝이 안맞는 경우
                correct = 0
                break
    if len(lst) != 0:   # 모두 확인했는데 짝이 없는 경우 오류!
        correct = 0
    
    print(f'#{case+1} {correct}')
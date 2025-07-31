# swea_4866 - 괄호검사 - D2

T = int(input())

for case in range(T):
    code = input()

    error = 1
    lst = []
    for s in code:
        if s == '(' or s == '{':
            lst.append(s)
        elif s == ')' or s == '}':
            if len(lst) == 0:
                error = 0
                break
            temp = lst.pop()
            if (s == ')' and temp != '(') or (s == '}' and temp != '}'):
                error = 0
                break
    if len(lst) != 0:
        error = 0
    
    print(f'#{case+1} {error}')
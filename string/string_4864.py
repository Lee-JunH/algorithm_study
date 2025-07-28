# swea - 문자열 비교 - D2

T = int(input())

for case in range(T):
    str1 = input()
    str2 = input()
    
    print(f'#{case+1} ', end='')
    if str1 in str2:
        print(1)
    else:
        print(0)
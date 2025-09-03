"""
SWEA_1240 - 단순 2진 암호코드 - D3

문제
- 암호코드는 8개의 숫자
- 암호코드에서의 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 가로길이는 56
- 올바른 암호코드 = (홀수 자리의 합 * 3) + (짝수 자리의 합) 이 10의 배수

"""

def find_code(code):
    secret = []
    for i in range(M):
        if code[i] == '1':
            for j in range(56):
                secret.append(code[i+j])
            break
    return list(reversed(secret))

def find_secret(s):
    if s == '0001101':
        return 0
    if s == '0011001':
        return 1
    if s == '0010011':
        return 2
    if s == '0111101':
        return 3
    if s == '0100011':
        return 4
    if s == '0110001':
        return 5
    if s == '0101111':
        return 6
    if s == '0111011':
        return 7
    if s == '0110111':
        return 8
    if s == '0001011':
        return 9
    

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    
    test = [list(input().strip()) for _ in range(N)]

    for t in test:
        if '1' in t:
            secret_code = find_code(list(reversed(t)))
            break
    result = []
    for i in range(0, 56, 7):
        secret = secret_code[i:i+7]
        result.append(find_secret(''.join(secret)))
    even = 0    #짝수
    odd = 0     #홀수
    for i in range(8):
        if i % 2 == 0:
            even += int(result[i])
        else:
            odd += int(result[i])
    final = even * 3 + odd
    print(f'#{case+1}', end=' ')
    if final % 10 == 0:
        print(odd+even)
    else:
        print(0)
"""
SWEA_1242 - 암호코드 스캔 - D5

문제
- 총 8개의 숫자로 이루어져 있다.
- 앞 7자리는 상품 고유의 번호를 나타내며, 마지막 자리는 검증 코드를 나타낸다.
- 검증 코드는 (홀수 합) * 3 + 짝수 합 + 검증코드 가 10의 배수
- 
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
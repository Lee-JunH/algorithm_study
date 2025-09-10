"""
SWEA_18613 - 16진수 암호비트패턴 출력하기
"""

def decimal_to_bin(n):
    bin = []
    for _ in range(4):
        bin.append(n%2)
        n //= 2
    return list(reversed(bin))

def hexa_to_bin(num):
    hexadecimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(16):
        if num == hexadecimal[i]:
            return decimal_to_bin(i)

T = int(input())
for case in range(T):
    hexa = list(input().strip())

    trf = []
    for h in hexa:
        trf.extend(hexa_to_bin(h))
    
    print(f'#{case+1}', end=' ')
    i = 0
    while i < len(trf):
        temp = trf[i:i+6]
        if temp == [0,0,1,1,0,1]:
            print(0, end=' ')
            i = i+6
        elif temp == [0,1,0,0,1,1]:
            print(1, end=' ')
            i = i+6
        elif temp == [1,1,1,0,1,1]:
            print(2, end=' ')
            i = i+6
        elif temp == [1,1,0,0,0,1]:
            print(3, end=' ')
            i = i+6
        elif temp == [1,0,0,0,1,1]:
            print(4, end=' ')
            i = i+6
        elif temp == [1,1,0,1,1,1]:
            print(5, end=' ')
            i = i+6
        elif temp == [0,0,1,0,1,1]:
            print(6, end=' ')
            i = i+6
        elif temp == [1,1,1,1,0,1]:
            print(7, end=' ')
            i = i+6
        elif temp == [0,1,1,0,0,1]:
            print(8, end=' ')
            i = i+6
        elif temp == [1,0,1,1,1,1]:
            print(9, end=' ')
            i = i+6
        else:
            i += 1
    print()
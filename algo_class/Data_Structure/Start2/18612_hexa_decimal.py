"""
SWEA_18612 - 16진수를 10진수로 변환하기 - D2

문제
- 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하라
"""

def decimal_to_bin(num):
    bin = []
    for _ in range(4):
        bin.append(num%2)
        num //= 2
    return list(reversed(bin))

def hexa_to_bin(num):
    hexadecimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(16):
        if num == hexadecimal[i]:
            return decimal_to_bin(i)

def bin_to_decimal(bin, length):
    hap = 0
    for i in range(length):
        hap += 2**i * bin[length-1-i]
    return hap

T = int(input())
for case in range(T):
    hexa = list(input().strip())

    bit = []
    for n in hexa:
        bit.extend(hexa_to_bin(n))
    
    print(f'#{case+1}', end=' ')
    i = 0
    len_total = len(bit)
    while i < len_total:
        if len_total - i >= 7:
            print(bin_to_decimal(bit[i:i+7], 7), end=' ')
            i += 7
        else:
            left = len_total-i
            print(bin_to_decimal(bit[i:], left), end=' ')
            i += left
    print()
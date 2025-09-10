"""
SWEA_3143 - 가장 빠른 문자열 타이핑 - D4

문제
- A의 길이만큼 키를 누르지 않고 어떤 문자열 B가 저장되어 있어 키를 한번 누른 것으로 B를 타이핑 할 수 있다.
- A전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.

풀이
- KMP 알고리즘을 이용하여 A와 B를 비교하고 같으면 다음 문자로 넘어간다.
"""

T = int(input())
for case in range(T):
    A, B = input().split()
    len_a = len(A)
    len_b = len(B)

    result = 0
    i = 0
    while i < len_a:
        if A[i] == B[0] and len_a >= i + len_b:
            count = 0
            for j in range(len_b):
                if A[i+j] == B[j]:
                    count += 1
                else:
                    break
            if count == len_b:
                i += j
        result += 1
        i += 1
    print(f'#{case+1} {result}')
"""
SWEA_4864 - 문자열 비교 - D2

문제
- 2개의 문자열에서 일치하는 부분이 있는지 확인하라
출력
- 존재하면 1, 존재하지 않으면 0

풀이
- Brute Force를 이용하여 같은 부분을 찾고 일치하지 않은 경우 다시 처음으로 돌아간다.
"""

T = int(input())
for case in range(T):
    str1 = input()
    str2 = input()

    i_1 = 0
    i_2 = 0
    len1 = len(str1)
    len2 = len(str2)

    while i_1 < len1 and i_2 < len2:
        if str1[i_1] == str2[i_2]:
            i_1 += 1
            i_2 += 1
        else:
            i_1 = 0
            i_2 += 1
    if i_1 == len1 : result = 1
    else : result = 0
    print(f'#{case+1} {result}')


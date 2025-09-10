"""
SWEA_4865 - 글자 수 - D2

문제
2개의 문자열에서 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력하라

풀이
Brute Force를 사용하여 한 칸씩 확인하며 count 후, 다른 문자를 만나면 max값 비교
"""

T = int(input())
for case in range(T):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)
    i_1 = 0
    i_2 = 0
    count = 0
    max_count = 0
    while True:
        if i_2 == M:
            if max_count < count:
                max_count = count
            i_1 += 1
            i_2 = 0
            count = 0
        if i_1 == N:
            break

        if str1[i_1] == str2[i_2]:
            count += 1
        i_2 += 1
    print(f'#{case + 1} {max_count}')



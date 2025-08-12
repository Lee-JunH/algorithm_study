"""
SWEA_4864 - 문자열 비교 - D2

문제
- 2개의 문자열에서 str2 안에 str1과 일치하는 부분이 있는지 찾아라

출력
- 존재하면 1
- 존재하지 않으면 0

풀이
- 브루트 포스로 처음부터 확인한다.
- KMP알고리즘으로 푼다.
"""

def lps(pattern):
    pi = [0] * len(pattern)

    i = 0
    check = 1
    for j in range(1, len(pattern)):
        while (i > 0 and pattern[j] != pattern[i]):
            i = pi[i-1]

        if pattern[i] == pattern[j]:
            pi[j] = i + 1
            i += 1
        
    return pi

T = int(input())
for case in range(T):
    str1 = input()
    str2 = input()

    print(lps())

print('iam im')
# T = int(input())
# for case in range(T):
#     str1 = input()
#     str2 = input()

#     if str1 in str2:
#         print(f'#{case+1} 1')
#     else:
#         print(f'#{case+1} 0')

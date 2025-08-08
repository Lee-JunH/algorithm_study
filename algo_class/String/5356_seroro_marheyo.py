"""
SWEA_5356 - 의석이의 세로로 말해요 - D3

문제
- 장난감 글자로 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9' 가 있다.
- 5개의 단어를 만들고 세로로 읽으려고 할 때 이를 공백 없이 출력하라

예외
- 각 단어의 개수가 다른 경우 해당 자리는 읽지 않고 다음 글자를 계속 읽는다.

풀이
- zip함수로 가능한지 확인하고 되면 zip으로 앞글자 출력
"""

T = int(input())
for case in range(T):
    word_ES = [list(input()) for _ in range(5)]

    dif = 0
    len_all = len(word_ES[0])
    for i in range(5):
        if len_all != len(word_ES[i]):
            dif = 1
        if len_all < len(word_ES[i]):
            len_all = len(word_ES[i])
    if dif == 0:
        print(f'#{case+1}', end=' ')
        for i in zip(*word_ES):
            print(''.join(i), end='')
        print()
    else:
        print(f'#{case + 1}', end=' ')
        for i in range(len_all):
            for s in word_ES:
                if i >= len(s):
                    continue
                print(s[i], end='')
        print()


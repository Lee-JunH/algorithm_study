"""
SWEA_1989 - 초심자의 회문 검사 - D2

문제
- 단어를 입력 받아 회문인지 확인

출력
- 회문이면 1 출력
- 회문이 아니면 0 출력

풀이
- 인덱스 슬라이싱 사용
"""

T = int(input())
for case in range(T):
    word = input()

    if word == word[::-1]:
        print(f'#{case+1} 1')
    else:
        print(f'#{case+1} 0')
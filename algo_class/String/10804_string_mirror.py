"""
SWEA_10804 - 문자열의 거울상 - D3

문제
- ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열을 거울에 비추면 어떤 문자열이 되는지 구하라

출력
- 뒤짚힌 문자열

풀이
- 거울에 비치면 b는 d로 d는 b로 p는 q로 q는 b로 변경된다.
- 딕셔너리로 키-값을 만들고 거꾸로 출력한다.
"""

T = int(input())
for case in range(T):
    str1 = input()

    my_dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    reverse_str1 = str1[::-1]
    print(f'#{case+1} ', end='')
    for s in reverse_str1:
        print(my_dict[s], end='')
    print()


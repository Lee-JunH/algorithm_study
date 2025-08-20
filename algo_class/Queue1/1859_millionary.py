"""
SWEA_1859 - 백만 장자 프로젝트 - D2

문제
- 연속된 N일 동안의 물건의 매매가를 예측할 수 있다.
- 하루에 최대 1만큼 구입할 수 있다. 판매는 언제든 가능

출력
- 최대 이익 출력

풀이
- max값을 찾고 앞의 값들을 다 빼준 후 max값 다음 리스트에서의 max값을 찾아 반복한다.
"""

T = int(input())
for case in range(T):
    N = int(input())
    product = list(map(int, input().split()))

    result = 0
    while len(product) > 1:
        max_v = 0
        max_i = 0
        for i in range(len(product)):
            if product[i] > max_v:
                max_v = product[i]
                max_i = i
        for j in range(max_i):
            result += max_v - product[j]
        product = product[max_i+1:]
    print(f'#{case+1} {result}')
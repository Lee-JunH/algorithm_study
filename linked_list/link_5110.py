"""
SWEA_5110 - 수열 합치기 - D3

문제
- 여러 개의 수열을 아래의 규칙에 따라 합친다.
    - 수열2의 첫 숫자보다 큰 숫자를 수열1에서 찾아 그 앞에 끼워 넣는다.
    - 큰 숫자가 없는 경우 맨 뒤에 붙인다.

출력
- 마지막 수열까지 합치고, 맨 뒤의 숫자부터 역순으로 10개 출력

풀이
- 앞 문제와 같이 찾은 숫자의 인덱스에 새로운 리스트 추가해준다.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


T = int(input())
for case in range(T):
    N, M = map(int, input().split())    # N: 수열의 길이, M: 수열의 개수
    suyeol = [list(map(int, input().split())) for _ in range(M)]

    result = suyeol[0].copy()
    for i in range(1, M):
        for j in range(N):
            if suyeol[i][0] < result[j]:
                result[j:j] = suyeol[i]
                break
        else:
            length = len(result)
            result[length:length] = suyeol[i]
    result = result[::-1]
    print(f'#{case+1}', end=' ')
    for k in range(10):
        if k >= len(result):
            break
        print(result[k], end=' ')
    print()
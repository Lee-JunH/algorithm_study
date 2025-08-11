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

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    suyeol = [list(map(int, input().split())) for _ in range(M)]

    for i in range(1, M):
        find = suyeol[i][0]
        index = -1
        for j in range(N):
            if suyeol[0][j] > find:
                index = j
                break
        if index == -1:
            suyeol[0].extend(suyeol[i])
        else:
            temp1 = suyeol[0][:index]  # index 앞 저장
            temp2 = suyeol[0][index:]  # index 뒤 저장
            temp1.extend(suyeol[i])
            temp1.extend(temp2)     # index 뒤 값 추가
            suyeol[0] = temp1
    print(f'#{case+1}', end=' ')
    result = suyeol[0][::-1]
    for k in range(10):
        print(result[k], end=' ')
    print()
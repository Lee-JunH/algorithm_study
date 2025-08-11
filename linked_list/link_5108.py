"""
SWEA_5108 - 숫자 추가 - D3

문제
- N개의 자연수로 이뤄진 수열이 주어질 때 M개의 숫자를 지정된 위치에 추가하면 완성된다.
- ex) 1 2 3 4 5 에서 2 7 입력 -> 1 2 7 3 4 5 출력

출력
- L 인덱스의 값 출력

풀이
- linked list로 구현하여 이전 값과 다음 값을 새로운 값과 연결해준다.
"""

T = int(input())
for case in range(T):
    N, M, L = map(int, input().split())
    suyeol = list(map(int, input().split()))

    for _ in range(M):
        index, num = map(int, input().split())

        temp1 = suyeol[:index]  # index 앞 저장
        temp2 = suyeol[index:]  # index 뒤 저장
        temp1.append(num)       # index 자리 num 추가
        temp1.extend(temp2)     # index 뒤 값 추가
        suyeol = temp1          # 수열 업데이트
    print(f'#{case+1} {suyeol[L]}')

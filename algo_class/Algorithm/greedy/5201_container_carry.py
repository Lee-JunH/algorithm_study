"""
SWEA_5201 - 컨테이너 운반 - D3

문제
- 화물에 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
- 트럭 당 한 개의 컨테이너 운반 할 수 있고, 적재용량을 초과하는 컨테이너는 운반 불가

- 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 구하는 문제
- 컨테이너를 한 개도 옮길 수 없는 경우 0 출력

풀이
- 트럭의 중량을 하나씩 보면서 트럭보다 작거나 같은것이 있으면 체크
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    total = 0
    container.sort(reverse=True)
    truck.sort()
    for i in range(M):
        for j in range(len(container)):
            if truck[i] >= container[j]:
                total += container[j]
                container.pop(j)
                break
    print(f'#{case+1} {total}')

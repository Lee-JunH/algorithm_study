"""
SWEA_5215 - 햄버거 다이어트 - D3

문제
- 민기의 햄버거 재료에 대한 점수와 가게에서 제공하는 재료에 대한 칼로리가 주어졌을 때
- 정해진 칼로리 이하의 조합 중에서 민기가 선호하는 햄버거를 조합하는 문제
- 햄버거의 선호도 : 조합된 재료들의 맛에 대한 점수의 합, 같은 재료 사용 X
"""

def backtrack(idx, taste, total_cal):
    global best_taste

    if total_cal > L:
        return

    if idx == N:
        best_taste = max(best_taste, taste)
        return
    
    backtrack(idx+1, taste + hamburger[idx][0], total_cal + hamburger[idx][1])
    backtrack(idx+1, taste, total_cal)

T = int(input())
for case in range(T):
    N, L = map(int, input().split())
    hamburger = [list(map(int, input().split())) for _ in range(N)]

    best_taste = 0
    backtrack(0, 0, 0)

    print(f'#{case+1} {best_taste}')
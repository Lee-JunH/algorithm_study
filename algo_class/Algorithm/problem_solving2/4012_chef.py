"""
SWEA_4012 - 요리사 - 모의 SW 역량테스트

문제
- N개의 식재료를 N/2개씩 나누어 2개의 요리를 하려고 한다.
- A음식과 B음식의 맛 차이가 최소가 되도록 재료를 배분해야 한다.
- 식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다.

풀이
- itertools로 구현하기
"""

from itertools import combinations

def taste(food):        # 재료 조합하기
    mat = 0
    for i in range(len(food)):
        for j in range(i+1, len(food)):
            ingredient1 = food[i]
            infredient2 = food[j]
            mat += arr[ingredient1][infredient2] + arr[infredient2][ingredient1]
    return mat

def calculate(food1, food2):   #   재료 조합하기
    global min_cha

    taste1 = taste(food1)
    taste2 = taste(food2)

    cha = abs(taste1 - taste2)
    min_cha = min(min_cha, cha)


T = int(input())
for case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cha = float('inf')

    for food1 in combinations(range(N), N//2):
        food2 = [i for i in range(N) if i not in food1]
        calculate(food1, food2)
    
    print(f'#{case+1} {min_cha}')
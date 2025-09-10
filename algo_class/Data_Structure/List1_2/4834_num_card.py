"""
SWEA_4834 - 숫자카드 - D2

문제 설명
- 0~9의 숫자가 적힌 N장의 카드에서 가장 많은 카드에 적힌 숫자와 카드 수 출력
"""

T = int(input())
for case in range(T):
    N = int(input())
    card = input()

    count_card = [0] * 10
    for num in card:
        count_card[int(num)] += 1
    max_count = 0
    for i in range(10):
        if count_card[i] >= max_count:
            max_card = i
            max_count = count_card[i]
    print(f'#{case+1} {max_card} {max_count}')


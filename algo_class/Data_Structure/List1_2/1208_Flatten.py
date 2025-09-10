"""
SWEA_1208 - Flatten - D3

문제 설명
- 노란색 상자들의 최고점과 최저점의 간격을 줄이는 작업을 시행한다.
- 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
"""


def my_max(box):
    max_box = 0
    max_index = 0
    for i in range(len(box)):
        if box[i] > max_box:
            max_box = box[i]
            max_index = i
    return max_box, max_index


def my_min(box):
    min_box = 100
    min_index = 0
    for i in range(len(box)):
        if box[i] < min_box:
            min_box = box[i]
            min_index = i
    return min_box, min_index


T = 10
for case in range(T):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        max_box, max_index = my_max(box)
        min_box, min_index = my_min(box)
        if max_box - min_box <= 1:
            break
        box[max_index] -= 1
        box[min_index] += 1
    a = my_max(box)[0]
    b = my_min(box)[0]
    result = a - b
    print(f'#{case+1} {result}')

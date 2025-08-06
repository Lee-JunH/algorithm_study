import sys

# 현재 파일과 같은 위치에 있는 input.txt파일 열어서 input으로 사용
sys.stdin = open('input.txt')
# input() 호출 시 'input.txt' 의 한 줄 씩 읽어서 가져옴
# input 함수는 리턴값이 문자열!!

# 테스트 케이스 개수 설정


# def falling(box, index, N, count):
#     j = index + 1
#     while j < N:
#         if box[index] > box[j]:
#             count += 1
#         elif box[index] == box[j]:
#             count += falling(box, j, N, 0)
#             break
#         j += 1
#     return count


T = int(input())
for case in range(T):
    N = int(input())    # 방의 가로 길이
    box_list = list(map(int, input().split()))

    max_fall = 0
    for i in range(N):
        count = 0
        j = i + 1
        for j in range(i+1, N):
            if box_list[i] > box_list[j]:
                count += 1
        if max_fall < count:
            max_fall = count
    print(f'#{case+1} {max_fall}')


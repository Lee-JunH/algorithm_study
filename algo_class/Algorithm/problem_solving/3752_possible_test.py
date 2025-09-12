"""
SWEA_3752 - 가능한 시험 점수 - D4

문제
- N개의 문제가 있다.
- 틀리면 0점 맞으면 배점만큼의 점수를 받게 된다.
- 학생들이 받을 수 있는 점수로 가능한 경우의 수는 몇가지 인가
"""

def get_score(s):
    for i in range(len(rst)):
        tmp = rst[i] + s
        rst.add(tmp)

T = int(input())
for tc in range(T):
    N = int(input())
    score_list = list(map(int, input().split()))

    rst = set([0])
    for i in range(N):
        get_score(score_list[i])
    print(f'#{tc+1} {len(rst)}')

# T = int(input())
# for case in range(T):
#     N = int(input())
#     test = list(map(int, input().split()))

#     dp = set()
#     count = 0
#     for i in range(N):
#         pass
#         # set에 저장해놓기
#         # set에 없는지 확인하기


# def dfs(idx, hap):
#     if idx == N:
#         my_grade.add(hap)
#         return
#     dfs(idx+1, hap+test[idx])
#     while idx < N:
#         if test[idx] == test[idx+1]:
#             idx += 1
#     dfs(idx+1, hap)

# T = int(input())
# for case in range(T):
#     N = int(input())
#     test = list(map(int, input().split()))

#     my_grade = set()
#     test.sort()
#     dfs(0,0)
#     print(f'#{case+1} {len(my_grade)}')
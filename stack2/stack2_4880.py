"""
SWEA_4880 - 토너먼트 카드 게임 - D2

문제 설명
- 가위바위보가 그려진 카드를 이용해 토너먼트로 한명을 뽑는다.
- N명의 학생이 N장의 카드를 나눠 갖는다. 승자끼리 카드를 비교해서 이긴 사람이 최종 승자
"""

def rock_scissor_paper(boy, girl, rsp_lst):     # 2개의 인덱스 중 가위바위보를 이긴 인덱스를 리턴해주는 함수
    if rsp_lst[boy] == 1:
        if rsp_lst[girl] == 2:
            winner = girl
    elif rsp_lst[boy] == 2:
        if rsp_lst[girl] == 3:
            winner = girl
    elif rsp_lst[boy] == 3:
        if rsp_lst[girl] == 1:
            winner = girl
    else:
        winner = boy
    return winner

# 1 2 3 4  0 ~ 2  2 ~ 4
# 1 2 3    0 ~ 2  2 ~ 3
# 1 2 3 4 5  0 ~ 3 3 ~ 5
def divide_group(rsp_lst, N):
    if N % 2 == 0:
        a = N // 2
        b = N-1
    else:
        a = N // 2 + 1
        b = N

    if a > 2:
        win1 = divide_group(rsp_lst, a)
    elif a == 2:
        win1 = rock_scissor_paper(0, 1, rsp_lst)
    elif a == 1:
        win1 = 0

    if N - a > 2:
        win2 = divide_group(rsp_lst, a)
    elif b - a == 2:
        win2 = rock_scissor_paper(2, 3, rsp_lst)
    elif b - a == 1:
        win2 = 2
    return rock_scissor_paper(win1, win2, rsp_lst)


T = int(input())
for case in range(T):
    N = int(input())
    rsp_lst = list(map(int, input().split()))

    winner = divide_group(rsp_lst, N)
    print(f'#{case+1} {winner+1}')
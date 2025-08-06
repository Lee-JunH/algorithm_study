"""
SWEA_4880 - 토너먼트 카드 게임 - D2

문제 설명
- 가위바위보가 그려진 카드를 이용해 토너먼트로 한명을 뽑는다.
- N명의 학생이 N장의 카드를 나눠 갖는다. 승자끼리 카드를 비교해서 이긴 사람이 최종 승자
"""

def rock_scissor_paper(p1, p2, rsp_lst): # 가위바위보를 이긴 인덱스를 리턴해주는 함수
    winner = p1
    if rsp_lst[p1] == 1:
        if rsp_lst[p2] == 2:
            winner = p2
    elif rsp_lst[p1] == 2:
        if rsp_lst[p2] == 3:
            winner = p2
    elif rsp_lst[p1] == 3:
        if rsp_lst[p2] == 1:
            winner = p2
    return winner


def divide_group(rsp_lst, S, G):
    if G - S == 2:
        return rock_scissor_paper(S, S+1, rsp_lst)
    elif G - S == 1:
        return S
    
    if (G - S) % 2 == 1:
        win1 = divide_group(rsp_lst, S, (S+G)//2 + 1)
        win2 = divide_group(rsp_lst, (S+G)//2 + 1, G)
    else:
        win1 = divide_group(rsp_lst, S, (S+G)//2)
        win2 = divide_group(rsp_lst, (S+G)//2, G)

    return rock_scissor_paper(win1, win2, rsp_lst)


T = int(input())
for case in range(T):
    N = int(input())
    rsp_lst = list(map(int, input().split()))

    winner = divide_group(rsp_lst, 0, N)
    print(f'#{case+1} {winner+1}')
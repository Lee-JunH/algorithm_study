"""
SWEA_5207 - 이진 탐색 - D3

문제
- 서로 다른 정수 N개가 주어지면 정렬하여 리스트 A에 저장한다.
- 이후 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인한다.
- 탐색 구간의 시작과 끝을 l과 r이라고 하면, 중심 원소의 인덱스 m = (l+r)//2이고
- 이진 탐색의 왼쪽구간은 l~m-1, 오른쪽 구간은 m+1~r이 된다.
- M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 문제

풀이
- 
"""

def bin_search(l, r, check):
    global num, cnt2

    m = (l+r) // 2

    if l > r:
        return 0

    if l == r:
        if A[m] == num:
            return 1
        return 0

    if A[m] < num:
        if check == 1:
            cnt2 = 0
        return bin_search(m+1, r, 1)
    elif A[m] > num:
        if check == 0:
            cnt2 = 0
        return bin_search(l, m-1, 0)
    elif A[m] == num:
        return 1

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0
    for i in range(M):
        cnt2 = 1
        num = B[i]
        if bin_search(0, N-1, 2):
            if cnt2 == 1:
                cnt += 1
    print(f'#{case+1} {cnt}')
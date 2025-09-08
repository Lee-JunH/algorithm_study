"""
SWEA_2817 - 부분 수열의 합 - D3

문제
- N개의 자연수가 주어졌을 때 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 문제

풀이
- 조합을 구하는 문제이다. DFS로 풀자~
"""

def dfs(index, hap):
    global cnt

    if hap == K:
        cnt += 1
        return
    elif hap > K:
        return
    if index == N-1:
        return
    for i in range(index+1, N):
        dfs(i, hap+sequence[i])

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        dfs(i, sequence[i])
    print(f'#{case+1} {cnt}')
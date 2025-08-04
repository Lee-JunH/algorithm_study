"""
swea_4869 - 종이붙이기 - D2 

func의 기능
- N이라는 가로 길이에 대해 채울 수 있는 경우의 수

(10,20), (20,20)의 사각형으로 채울 수 있는 가로는
10, 20 2개지만 20은 10을 눕혀서 만들 수 있어 20인 경우 *2

재귀로 만들어서
N-10 즉 앞을 10으로 채운 경우
N-20 즉 20으로 채운 경우
남은 값이 0일 때는 모두 채웠으니 return 1
(-)값인 경우 못채우니까 return 0
"""

def func(N, count):
    if N == 0:
        return 1
    if N < 0:
        return 0
    count += func(N - 10, count) + 2 * func(N - 20, count)
    return count

T = int(input())
for case in range(T):
    N = int(input())

    result = []
    i = 0
    j = 0
    count = func(N, 0) 
            
    print(f'#{case+1} {count}')

"""
- 강의 내용 추가
1. recursive 방식 (재귀)
재귀적 구조는 내부에 시스템 호출 스택을 사용하는 overhead가 발생 가능

2. iterative 방식
Memorication응ㄹ 재귀적 구조에 사용하는 것보다 반복적 구조로
DP를 구현한 것이 성능 면에서 보다 효율적이다.
"""
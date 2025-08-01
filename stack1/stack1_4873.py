# swea_4873 - 반복문자 지우기 - D2

# 문제 : 문자열에서 반복된 문자를 지운다. 남은 문자열의 길이 출력
# 예시 : CAAABBA -> C(AA)ABBA -> CA(BB)A -> C(AA) -> C

T = int(input())

for case in range(T):
    iter_str = input()

    temp = []
    for s in iter_str:
        temp.append(s)
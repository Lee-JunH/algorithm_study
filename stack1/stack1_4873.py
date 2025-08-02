# swea_4873 - 반복문자 지우기 - D2

# 문제 : 문자열에서 반복된 문자를 지운다. 남은 문자열의 길이 출력
# 예시 : CAAABBA -> C(AA)ABBA -> CA(BB)A -> C(AA) -> C

T = int(input())

# def my_len(length):
#     count = 0
#     for _ in length:
#         count += 1
#     return count

for case in range(T):
    text = list(input())

    i = 0
    while i < len(text) - 1:
        if text[i] == text[i+1]:
            text.pop(i)
            text.pop(i)
            if i == 0:
                i -= 1
            else:
                i -= 2
        i += 1
    
    print(f'#{case+1} {len(text)}')


# 10개 중 9개 맞음

# T = int(input())
# for case in range(T):
#     text = list(input())

#     i = 0
#     while i < len(text) - 1:
#         if text[i] == text[i+1]:
#             text.pop(i)
#             text.pop(i)
#             i -= 2
#         i += 1

#     print(f'#{case+1} {len(text)}')
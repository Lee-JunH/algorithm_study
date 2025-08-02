# swea_4873 - 반복문자 지우기 - D2

# 문제 : 문자열에서 반복된 문자를 지운다. 남은 문자열의 길이 출력
# 예시 : CAAABBA -> C(AA)ABBA -> CA(BB)A -> C(AA) -> C


# def my_len(length):
#     count = 0
#     for _ in length:
#         count += 1
#     return count

T = int(input())
for case in range(T):
    text = list(input())

    i = 0
    while i < len(text) - 1:
        if text[i] == text[i+1]:    # 붙어있는 값이 같을 때
            text.pop(i) # 2번 pop하여 제거
            text.pop(i)
            if i == 0:  # 첫번째인 경우는 i 값 유지 (-1 +1)
                i -= 1
            else:       # 그 외는 한칸 뒤로 (-2 +1)
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
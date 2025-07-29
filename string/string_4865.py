# swea_4865 - 글자수 - D2

T = int(input())

for case in range(T):
    str1 = input()
    str2 = input()

    my_dict = {}
    for s1 in str1:
        count = 0
        for s2 in str2:
            if s1 == s2:
                count += 1
        my_dict.setdefault(s1, count)
    # max_str = 0
    # for value in my_dict.values():
    #     if max_str < value:
    #         max_str = value
    max_str = max(my_dict.values())
    print(f'#{case+1} {max_str}')
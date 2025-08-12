"""
SWEA_5432 - 쇠막대기 자르기 - D4

문제
- 효율적인 작업을 위해 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 자른다.
- 레이저는 (), 쇠막대기는 (()) 일 때 바깥 괄호이다.
- 조건
    - 자신보다 긴 쇠막대기 위에만 놓을 수 있다.
    - 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
    - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
    - 레이저는 어떤 쇠막대기의 양 긑점과도 겹치지 않는다.

출력
- 잘려진 쇠막대기 조각의 총 개수를 구하라

풀이
- 레이저를 쏘고 닫을 때는 지금까지 쌓인 '('의 개수만큼 쇠막대기가 생성된다.
- 일반적으로 닫을 때는 쇠막대기가 하나씩 더해진다.
- 이것을 이용해 풀이.
"""

T = int(input())
for case in range(T):
    paran = input()

    count = 0
    result = 0
    my_stack = []
    for p in paran:
        if p == '(':
            my_stack.append(p)
            raser = 1
            count += 1
        else:
            temp = my_stack.pop()
            count -= 1
            if raser == 1:
                result += count
            else:
                result += 1
            raser = 0 
    
    print(f'#{case+1} {result}')
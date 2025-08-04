"""
swea_4871 - 그래프 경로 - D2

문제 설명 - 출발1, 도착 8
1 -> 2,3  3-> 4,9  9-> 7,8  인 경우 최종 1->3->9->8
"""

T = int(input())

def recursion(my_dict, s_node, g_node, exist):
    # 노드의 경로가 저장된 my_dict, 출발 노드 s_node, 도착 노드 g_node
    for node in my_dict[s_node]:    #출발 노드에 있는 경로들 확인
        if node == g_node:  # 도착 노드로 연결되어 있으면 1 출력
            return 1
        else:
            if node in my_dict:
                exist = recursion(my_dict, node, g_node, exist)
                if exist == 1:
                    return exist
            else:   # 만약 현재 노드에서 더이상 갈 곳이 없는 경우
                return 0
    return exist

for case in range(T):
    V, E = map(int, input().split())    # V : 총 노드 수, E : 연결 된 노드 수

    my_dict = {}                        # dict형으로 연결된 경로 저장
    for _ in range(E):
        a, b = map(int, input().split())
        my_dict.setdefault(a,[])        # 노드가 저장되어 있으면
        my_dict[a].append(b)            # 그 노드에 저장
    S, G = map(int, input().split())    

    exist = recursion(my_dict, S, G, 0) # 재귀의 입력값으로 dict, 출발지점, 도착지점 전달
    print(f'#{case+1} {exist}')

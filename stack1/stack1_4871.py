# swea_4871 - 그래프 경로 - D2

T = int(input())

def dfs(my_dict, s_node, g_node, exist):
    for node in my_dict[s_node]:
        if node == g_node:
            return 1
        else:
            if node in my_dict:
                exist = dfs(my_dict, node, g_node, exist)
                if exist == 1:
                    return exist
            else:
                return 0
    return exist

for case in range(T):
    V, E = map(int, input().split())

    my_dict = {}
    for _ in range(E):
        a, b = map(int, input().split())
        my_dict.setdefault(a,[])
        my_dict[a].append(b)
    S, G = map(int, input().split())

    exist = dfs(my_dict, S, G, 0)
    print(f'#{case+1} {exist}')

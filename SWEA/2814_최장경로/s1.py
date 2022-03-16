import sys
sys.stdin = open('input.txt')


def dfs(v, cost):
    global max_length, visited2

    visited[v] = 1

    for w in range(1, N+1):
        if adj_list[v][w] and not visited[w]:

            visited[w] = 1

            dfs(w, cost+1)
            visited[w] = 0

    if max_length < cost:
        max_length = cost



T = int(input())

for tc in range(1, T+1):
    # N : 정점 수, M : 간선수
    N, M = map(int, input().split())
    adj_list = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        n1, n2 = map(int, input().split())
        adj_list[n1][n2] = 1
        adj_list[n2][n1] = 1

    max_length = 0

    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i, 1)
    print('#{} {}'.format(tc, max_length))
import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(n, cnt):
    global ans
    queue = deque()
    queue.append((N, cnt))
    visited[n] = 1

    while queue:
        n, cnt = queue.popleft()

        if n == M:
            ans = cnt
            return

        for i in range(len(operator_list)):
            if operator_list[i] == '*2':

                if 0 < 2*n <= 1000000 and not visited[2*n]:
                    queue.append((2*n, cnt+1))
                    visited[2*n] = 1
            else:
                if 0 < n + operator_list[i] <= 1000000 and not visited[n + operator_list[i]]:
                    queue.append((n + operator_list[i], cnt+1))
                    visited[n + operator_list[i]] = 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    operator_list = [1, -1, '*2', -10]
    ans = 0

    bfs(N, 0)
    print('#{} {}'.format(tc, ans))
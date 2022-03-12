from collections import deque

arr = [-1, 1]
answer = 0


def bfs(numbers, N, target):
    global arr
    global answer

    queue = deque()
    queue.append((0, 1))

    while queue:
        num, n = queue.popleft()

        if n - 1 == N:
            if num == target:
                answer += 1
        else:
            for i in range(2):
                queue.append((num + (numbers[n - 1] * arr[i]), n + 1))


def solution(numbers, target):
    N = len(numbers)

    bfs(numbers, N, target)

    return answer
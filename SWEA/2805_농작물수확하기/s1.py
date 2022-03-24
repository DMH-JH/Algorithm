import sys
sys.stdin = open('input.txt')

T = int(input())
for TC in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    c = N//2
    sum_value = 0
    for i in range(0, c + 1):
        for j in range(c-i, c+i+1):
            sum_value += arr[i][j]

    for i in range(c+1, N):
        for j in range(c-(N-1-i), c+(N-1-i)+1):
            sum_value += arr[i][j]

    print('#{} {}'.format(TC, sum_value))

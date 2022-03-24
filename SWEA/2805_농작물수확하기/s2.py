import sys
sys.stdin = open('input.txt')

T = int(input())
for TC in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    c = N//2
    a = 0
    for i in range(c+1):
        a += sum(arr[i][c-i:c+i+1])

    for j in range(c+1, N):
        a += sum(arr[j][c-(N-1-j):c+(N-1-j)+1])

    print('#{} {}'.format(TC, a))

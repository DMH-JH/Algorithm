import sys
sys.stdin = open('input.txt')

T = int(input())
for TC in range(1, T+1):
    # N : A의 길이
    # M : B의 길이
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        long_arr = A
        short_arr = B
    else:
        long_arr = B
        short_arr = A

    max_value = 0
    for i in range(len(long_arr)-len(short_arr)+1):
        sum_of_num = 0
        for k in range(len(short_arr)):
            sum_of_num = sum_of_num + (short_arr[k] * long_arr[i+k])
        if sum_of_num > max_value:
            max_value = sum_of_num

    print('#{} {}'.format(TC, max_value))
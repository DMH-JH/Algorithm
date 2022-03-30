
origin_W = [0] * 8
for i in range(0, 8, 2):
    origin_W[i] = 'WBWBWBWB'
    origin_W[i+1] = 'BWBWBWBW'


origin_B = [0] * 8
for i in range(0, 8, 2):
    origin_B[i] = 'BWBWBWBW'
    origin_B[i+1] = 'WBWBWBWB'

# M : 가로, N : 세로
N, M = map(int, input().split())

input_arr = [list(input()) for _ in range(N)]

min_cnt = 98776523423

for i in range(N-8+1):
    for j in range(M-8+1):
        w_cnt = 0
        b_cnt = 0
        for k in range(8):
            for l in range(8):
                if input_arr[i+k][j+l] != origin_W[k][l]:
                    w_cnt += 1

        for k in range(8):
            for l in range(8):
                if input_arr[i+k][j+l] != origin_B[k][l]:
                    b_cnt += 1

        if w_cnt < min_cnt:
            min_cnt = w_cnt

        if b_cnt < min_cnt:
            min_cnt = b_cnt


print(min_cnt)